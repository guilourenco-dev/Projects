package bci.core;

import bci.core.exception.*;
import java.io.*;
import java.util.List;

/**
 * The façade class. Represents the manager of this application. It manages the current
 * library and works as the interface between the core and user interaction layers.
 */
public class LibraryManager implements Serializable  {
  private static final long serialVersionUID = 2025102101L;

  private final Date _date = new Date(); 
  private int _userId; 
  private String _filename = null; 
  private Library _library ;
  
  
  /** The object doing all the actual work. */
  /* The current library */
  
  public LibraryManager() {
    _library = new Library();
    _userId = _library.getUserIdLibrary();
  }

  public String getFilename() { return _filename; }
  public User getUser(int idUser){ return _library.getUser(idUser);}
  public int getCurrentDate(){ return _library.getCurrentDate();} 
  public int getUserIdLibraryManager(){ return _library.getUserIdLibrary();}   
  public String getWorkDescription(int id) { 
    return _library.getWorkDescription(id);
  }
  public List<String> getWorkDescriptions() { 
    return List.copyOf(_library.getWorkDescriptions()); 
  }
  public Work getWork(int id) { return _library.getWork(id); }
  public List<Work> getWorks() { return List.copyOf(_library.getWorks()); }
  public List<String> getUserDescriptions() {
    return List.copyOf(_library.getUserDescriptions());
  }
  public String getUserDescription(int idUser) {
    return _library.getUserDescription(idUser);
  }
  public List<String> getDescriptionsByCreator(String name) {
    return List.copyOf(_library.getDescriptionsByCreator(name));
  }
  public String getUserName(int idUser){
    return _library.getUserName(idUser);
  }
  public List<Work> getWorksByCreator(String name) { 
  return List.copyOf(_library.getWorksByCreator(name));
  }
  public boolean isDirty() { return _library.isDirty(); }
  public int getLastFailedRuleId() { return _library.getLastFailedRuleId(); }

      
  public void setDirty(boolean dirty) { _library.setDirty(dirty); }
  public void setFilename(String filename) { _filename = filename; }


  public boolean hasAssociatedFile() { return _filename != null; } 
  
  public boolean findCreator(String name) {return _library.findCreator(name);}

  public boolean findUser(int idUser) {return _library.findUser(idUser);}

  public boolean findWork(int idWork) {return _library.findWork(idWork);}

  public void incrementUserIdLibraryManager(){_userId++;}
  

  /**
   * Advances the current date of the library by the given number of days.
   * This operation also marks the library as modified.
   * @param n the number of days to advance
   */
  public void advanceDays(int n) {
    _library.advanceDays(n);
    _date.advanceDays(n);
  }

  
  /**
   * Saves the serialized application's state into the file associated to the current library
   *
   * @throws FileNotFoundException if for some reason the file cannot be created or opened. 
   * @throws MissingFileAssociationException if the current library does not have a file.
   * @throws IOException if there is some error while serializing the state of the network to disk.
   **/
  public void save() throws IOException, MissingFileAssociationException{
    if (_filename == null) throw new MissingFileAssociationException();
    try (var out = new ObjectOutputStream(new BufferedOutputStream
    (new FileOutputStream(_filename)))) {
      out.writeObject(_library);
    } 
    setDirty(false);
  }

  /**
   * Saves the serialized application's state into the specified file. The current library is
   * associated to this file.
   *new DoOpenFile(receiver), //
                new DoSaveFile(receiver), //
                new DoDisplayDate(receiver), //
                new DoAdvanceDate(receiver), //
                new DoOpenMenuUsers(receiver), //
                new DoOpenMenuWorks(receiver), //
                new DoOpenMenuRequests(receiver) /
   * @param filename the name of the file.
   * @throws FileNotFoundException if for some reason the file cannot be created or opened.
   * @throws MissingFileAssociationException if the current library does not have a file.
   * @throws IOException if there is some error while serializing the state of the network to disk.
   **/
  public void saveAs(String filename) throws IOException {
    _filename = filename;
    try { save(); 
    } catch (MissingFileAssociationException | IOException e){ 
      _filename = null; 
    } 
  }

  
  /**
   * Register a user with given name and email.
   * @param name the user's name
   * @param email the user's email
   * @return the user's id
   */
  public int registerUser(String name, String email) {
    if (_userId != _library.getUserIdLibrary()){
      _userId = _library.getUserIdLibrary();}
    _library.registerUser(name, email);
    incrementUserIdLibraryManager();
    return _userId - 1;
  }
 

  /**
   * Loads the previously serialized application's state as set it as the current library.
   *
   * @param filename name of the file containing the serialized application's state
   *        to load.
   * @throws UnavailableFileException if the specified file does not exist or there is
   *         an error while processing this file.
   **/
  public void load(String filename) throws UnavailableFileException, 
  IOException {
    try (var in = new ObjectInputStream(new BufferedInputStream
    (new FileInputStream(filename)))) {
      _library = (Library) in.readObject();   
      _filename = filename;
      setDirty(false);
    } catch (ClassNotFoundException e) { throw new IOException(e); }
    catch (FileNotFoundException e) {
      throw new UnavailableFileException(filename); 
    }
  }


/**
 * Register a book with given id, price, number of copies, title, creators, category and isbn.
 * @param id the book's id
 * @param price the book's price
 * @param numOfCopies the number of copies of the book
 * @param title the book's title
 * @param creator the book's creators
 * @param category the book's category
 * @param isbn the book's isbn
 * @return the registered book
 */
  public Work registerBook(int id, int price, int numOfCopies, String title,
  Creator[] creator, Category category, String isbn) {
    Work work = _library.registerBook(id, price, numOfCopies, 
    title, creator, category, isbn);
    return work;
  }


/**
 * Register a DVD with given id, price, number of copies, title, creators, category and IGAC.
 * @param id the DVD's id
 * @param price the DVD's price
 * @param numOfCopies the number of copies of the DVD
 * @param title the DVD's title
 * @param creator the DVD's creators
 * @param category the DVD's category
 * @param igac the DVD's IGAC
 * @return the registered DVD
 */
  public Work registerDvd(int id, int price, int numOfCopies, String title,
  Creator[] creator, Category category, String igac){
    Work work = _library.registerDvd(id, price, numOfCopies, 
    title, creator, category, igac);
    return work;
  }


  /**
   * Read text input file and initializes the current library (which should be empty)
   * with the domain entities representeed in the import file.
   *
   * @param datafile name of the text input file
   * @throws ImportFileException if some error happens during the processing of the
   * import file.
   **/
  public void importFile(String datafile) throws ImportFileException {
    try {
      // reset to a fresh library before importing so the import initializes a clean state
      _library = new Library();
      // delegate parsing to Library.importFile which uses MyParser internally
      _library.importFile(datafile);
      // after a successful import, this manager no longer has an associated serialized file
      _filename = null;
      // keep manager's user id in sync with library
      _userId = _library.getUserIdLibrary();
    } catch (IOException | UnrecognizedEntryException e) {
      throw new ImportFileException(datafile, e);
    }
  }

/**
 * Searches for works whose descriptions contain the given term.
 * @param term the term to search for
 * @return a list of descriptions of the works that contain the given term
 */
  public List<String> searchWorks(String term) {
    return _library.searchWorks(term);
  }
  

/**
 * Requests a work to be borrowed by a user.
 * @param userId the user ID
 * @param workId the work ID
 * @return the deadline of the request
 * @throws NoSuchUserCoreException if the user with the given ID does not exist
 * @throws NoSuchWorkCoreException if the work with the given ID does not exist
 * @throws BorrowingRuleFailedCoreException if the borrowing rule fails
 */
  public int requestWork(int userId, int workId) 
            throws BorrowingRuleFailedCoreException, 
            NoSuchUserCoreException, NoSuchWorkCoreException, 
            WorkNotBorrowedByUserCoreException {
    if (!_library.findUser(userId)) {
        throw new NoSuchUserCoreException(userId);
    }
    if (!_library.findWork(workId)) {
        throw new NoSuchWorkCoreException(workId);
    }
    return _library.requestWork(getUser(userId), getWork(workId));     
  }

    
/**
 * Returns a work by a user. The work must be in the library, the user must exist and the work must have been borrowed by the user.
 * @param userId the id of the user who is returning the work
 * @param workId the id of the work being returned
 * @return the work's id
 * @throws NoSuchUserCoreException if the user does not exist
 * @throws NoSuchWorkCoreException if the work does not exist
 * @throws WorkNotBorrowedByUserCoreException if the work was not borrowed by the user
 */
  public int returnWork(int userId, int workId)
      throws NoSuchUserCoreException, NoSuchWorkCoreException, 
      WorkNotBorrowedByUserCoreException {
      
      if (!_library.findUser(userId)) {
          throw new NoSuchUserCoreException(userId);
      }
      User user = getUser(userId);

      if (!_library.findWork(workId)) {
          throw new NoSuchWorkCoreException(workId);
      }
      Work work = getWork(workId);
      
      try {
      return _library.returnWork(user, work);
      } catch (WorkNotBorrowedByUserCoreException  e) {
          throw new WorkNotBorrowedByUserCoreException(userId, workId);
      }
  }

/**
 * Pays the fine of a user.
 * @param userId the id of the user whose fine to pay
 * @throws UserIsActiveCoreException if the user is active and therefore cannot pay the fine
 * @throws NoSuchUserCoreException if the user does not exist
 */
  public void payFine(int userId) throws UserIsActiveCoreException, NoSuchUserCoreException {
    if (!_library.findUser(userId)) throw new NoSuchUserCoreException(userId);
    User user = getUser(userId); 
    if (user.isActive()) {
        throw new UserIsActiveCoreException(userId);
    }
    user.clearFine();
    if (!user.hasOverdue(getCurrentDate())) user.setActive(true);
    _library.setDirty(true); 
}




/**
 * Registers the user with the given user ID as being interested in the availability
 * of the work with the given work ID.
 * @param uid the user ID
 * @param wid the work ID
 * @throws NoSuchUserCoreException if the user with the given ID does not exist
 * @throws NoSuchWorkCoreException if the work with the given ID does not exist
 */
public void registerAvailabilityInterest(int userId, int workId) {
  _library.registerAvailabilityInterest(getUser(userId), getWork(workId));
}


/**
 * Changes the number of available copies of a work by a given delta.
 * @param wid the work ID
 * @param delta the number of copies to add or remove
 * @return true if the operation was successful, false otherwise
 * @throws NoSuchWorkCoreException if the work does not exist
 */
public boolean changeCopies(int wid, int delta) 
throws NoSuchWorkCoreException{
  if (!_library.findWork(wid)) throw new NoSuchWorkCoreException(wid);
  return _library.changeCopies(wid, delta);
}

/**
 * Consumes all notifications for a given user.
 * @param uid the user ID
 * @return a list of strings representing the notifications
 * @throws NoSuchUserCoreException if the user does not exist
 */
public List<String> consumeUserNotifications(int uid)
    throws NoSuchUserCoreException {
  if (!_library.findUser(uid)) throw new NoSuchUserCoreException(uid);
  var u = getUser(uid);
  return u.consumeNotifications().stream().map(Object::toString).toList();
}
}