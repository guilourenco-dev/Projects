package bci.core;

import bci.core.exception.*;
import bci.core.rules.*;
import bci.core.behaviors.UserBehavior;
import bci.core.behaviors.Normal;
import bci.core.behaviors.Cumpridor;

import java.io.*;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.Collections;

public class Library implements Serializable { 

  @Serial
  private static final long serialVersionUID = 202501101348L;
  private final List<User> _userList = new ArrayList<>();
  private int _currentDate = 1;
  private int _userId = 1; 
  private boolean _dirty;

  private final Map<Integer, Work> _works = new HashMap<>();  
  private final Map<String, Creator> _creatorsByName = new HashMap<>();
  private int _nextCreatorId = 1; 
  private int _nextWorkId = 1; 

  private final List<Rule> _rules;
  private int _lastFailedRuleId = 0;

  private final List<Request> _allOpenRequests = new ArrayList<>();

  // Constructor
  public Library() {
    _dirty = false;

    _rules = new ArrayList<>();
        _rules.add(new Rule01());
        _rules.add(new Rule02());
        _rules.add(new Rule03());
        _rules.add(new Rule04());
        _rules.add(new Rule05());
        _rules.add(new Rule06());

        Collections.sort(_rules);
      
  }
  /**1ª Tarefa:
   * Acrescente uma nova restrição no dominio do problema que impede a biblioteca de ter mais do que 12 requisicoes de obra em cada momento. Caso esta regra de negócio seja violada, então o comando Requisitar Obra deve lançar a excecao WorkNotBorrwoedByUserException, indicando as chaves do utente e da obra indicadas pelo utilizador
   * 2ª Tarefa: Concretize uma nova operacao, com o tiltulo "Apresenta utentes com dívida maior"
 no menu Gestao de Utentes que apresenta todos os utentes que têm uma ulta por pagar amior ou igual a um determinado valor. Este valor deve ser pedido ao utilizador. O comando deve apresentar primeiro o número de utentes que verificam esta codniçao seguido dos utentes que verificam a condicao. Os utentes devem ser apresentados por ordem decrescente do valor da multa. Para cada utente devem ser apresentados o valor da multa e o seu nome 
 3ª Tarefa: Acrescente um novo comando, com o nome "Utente com maior valor", no menu de Gestão de utentes. Este comando deve indicar o nome do utente com o maior valor em obras requisitadas. Caso haja dois utentes com o mesmo valor máximo, então deve considerar o que tem o nome menor. Se tiverem o mesmo tamanho, então considere apenas um deles. O comando deve apresentar o id do utente e valor máximo das obras requisitadas. Se não houver utentes com obras requisitdas, entao o comando deve escrever a mensagem "Sem obras"*/

  boolean isDirty() { return _dirty; }
  public int getCurrentDate(){ return _currentDate; } 
  public int getNextWorkId(){ return _nextWorkId++; }
  List<User> getUserList(){ return List.copyOf(_userList); }
  public int getUserIdLibrary(){ return _userId; } 
  Work getWork(int id){ return _works.get(id); }
  public int getLastFailedRuleId() { return _lastFailedRuleId; }
  public String getUserName(int idUser){
    for (User user : _userList){
      if (user.getUserId() == idUser)
      return user.getUserName();
    }
    return null;
  }


void setDirty(boolean dirty) { _dirty = dirty; }
void incrementUserIdLibrary(){_userId++;}
boolean findWork(int id){ return _works.containsKey(id); }
void registerAvailabilityInterest(User u, Work w) { w.addInterested(u);}



/**
 * Advances the library's current date by the given number of days.
 * @param n the number of days to advance
 */
  void advanceDays(int n){  
    if (n > 0) _currentDate += n;
    for (User u : _userList) {        
      boolean overdue = u.hasOverdue(_currentDate);
      boolean hasFine = u.getUserFine() > 0;
      u.setActive(!(overdue || hasFine));
    }
    setDirty(true);
  }
  

/**
 * Adds a work to the library.
 * @param work the work to be added
 */
  public void addWork(Work work) { 
    _works.put(work.getWorkId(), work);
    setDirty(true);
  } 

/**
 * Parse a string as an integer.
 * If the string does not contain a valid integer, throw an UnrecognizedEntryException.
 * @param str the string to be parsed
 * @param field the field name in which the string is located
 * @param line the line of text in which the string is located
 * @return the integer value of the parsed string
 * @throws UnrecognizedEntryException if the string is not a valid integer
 */
int parseInt(String str, String field, String line) 
throws UnrecognizedEntryException {
    try { return Integer.parseInt(str.trim()); }
    catch (NumberFormatException e) {
      throw new UnrecognizedEntryException
      ("inteiro inválido no campo '" + field + "': " + line, e);
    }
  }


/**
 * Checks if a creator with the given name exists in the library.
 * @param name the name of the creator to be searched
 * @return true if the creator exists, false otherwise
 */
  boolean findCreator(String name) {
    return _creatorsByName.containsKey(name.trim());
  }


/**
 * Checks if a user with the given id exists in the library.
 * @param idUser the id of the user to be searched
 * @return true if the user exists, false otherwise
 */
  boolean findUser(int idUser) {
    for (User user : _userList){
      if (user.getUserId() == idUser)
      return true;
    }
    return false;
  }


/**
 * Returns a list of all the works registered in the library.
 * The list is ordered by the id of the works.
 * @return a list of all the works registered in the library
 */
  List<Work> getWorks() { 
    List<Work> list = new ArrayList<>(_works.values()); 
    list.sort((work1, work2) -> Integer.compare(work1.getWorkId(),
    work2.getWorkId())); 
    return List.copyOf(list);
    
  }


/**
 * Returns a list of works created by the given creator.
 * The list is ordered by the id of the works.
 * @param name the name of the creator
 * @return a list of works created by the given creator
 */
  List<Work> getWorksByCreator(String name) {
    var out = new ArrayList<Work>();
    for (Work work : _works.values()) {                            
      for (Creator creator : work.getCreator()) {      
        if (creator.getName().equalsIgnoreCase(name)) {    
            if (work.getAvailableCopies() > 0)
              out.add(work);                                     
        }
      }
    }
    out.sort(Comparator.comparing(w -> w.getTitle().toLowerCase())); 
    return List.copyOf(out);
  }


/**
 * Returns a list of descriptions of all the works created by the given creator.
 * The descriptions are retrieved from the works registered in the library that have the given creator.
 * @param name the name of the creator
 * @return a list of descriptions of all the works created by the given creator
 */
  List<String> getDescriptionsByCreator(String name) {
    List<String> desc = new ArrayList<>();
    for (Work work : getWorksByCreator(name)) { 
    desc.add(work.getDescription());
    }
  return List.copyOf(desc);
  }

/**
 * Returns a list of descriptions of all the works in the library.
 * The list is ordered by the id of the works.
 * @return a list of descriptions of all the works in the library
 */
  List<String> getWorkDescriptions() {
    List<String> desc = new ArrayList<>();
    for (Work work : getWorks()) { 
    desc.add(work.getDescription());
    }
  return List.copyOf(desc);
  }


/**
 * Returns the description of the work with the given id.
 * If there is no work with the given id, returns a message indicating that the work does not exist.
 * @param id the id of the work to be retrieved
 * @return the description of the work with the given id, or a message indicating that the work does not exist
 */
  String getWorkDescription(int id){      
    for (Work work : _works.values()){
      if (work.getWorkId() == id)
        return work.getDescription();
    }
    return "A obra " + id + " não existe.";
  }
  


/**
 * Register a book with given id, price, number of copies, title, creators, category and isbn.
 * If there are multiple creators, register all of them.
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
    if (creator.length > 1) {
      for (Creator creat : creator) { 
        registerCreator(creat.getName()); 
      }
    } else {
    registerCreator(creator[0].getName());
    }
    Work work = new Book(id, price, numOfCopies, title , 
    creator, isbn, category);   
    _works.put(work.getWorkId(), work);
    setDirty(true);
    return work;
  }


/**
 * Register a DVD with given id, price, number of copies, title, creators, category and IGAC.
 * @param id the DVD's id
 * @param price the DVD's price
 * @param numOfCopies the number of copies of the DVD
 * @param title the DVD's title
 * @param creator the DVD's creator
 * @param category the DVD's category
 * @param igac the DVD's IGAC
 * @return the registered DVD
 */
  public Work registerDvd(int id, int price, int numOfCopies, String title,
  Creator[] creator, Category category, String igac) {
    registerCreator(creator[0].getName());
    Work work = new Dvd(id, price, numOfCopies, title, 
    creator, igac, category);   
    _works.put(work.getWorkId(), work);
    setDirty(true);
    return work;
  }



/**
 * Registers a creator with the given name.
 * If the creator already exists, it is retrieved from the library.
 * If the creator does not exist, a new one is created and registered in the library.
 * @param name the name of the creator
 * @return the registered creator
 */
  public Creator registerCreator(String name) {
    String key = name == null ? "" : name.trim().replaceAll("\\s+", " ");
    Creator creator = _creatorsByName.get(key);
    if (creator == null) {
      creator = new Creator(_nextCreatorId++, key);
    _creatorsByName.put(key, creator);
    }
    setDirty(true);
    return creator;
  }


/**
 * Returns the description of the user with the given id.
 * If there is no user with the given id, returns a message indicating that the user does not exist.
 * @param idUser the id of the user to be retrieved
 * @return the description of the user with the given id, or a message indicating that the user does not exist
 */
  String getUserDescription(int idUser) {
    for (User user : _userList){
      if (user.getUserId() == idUser)
      return user.getDescription();
    }
    return "O utilizador " + idUser + " não existe.";
  }
  
/**
 * Returns a creator with the given name.
 * If the creator already exists, it is retrieved from the library.
 * If the creator does not exist, a new one is created and registered in the library.
 * @param name the name of the creator
 * @return the registered creator
 */
  public Creator getCreator(String name) {
  String key = name.trim();
  Creator c = _creatorsByName.get(key);
  if (c == null) {
    c = new Creator(_nextCreatorId++, key);
    _creatorsByName.put(key, c);
  }
  return c;
}

/**
 * Returns a list of descriptions of all the users registered in the library.
 * The list is ordered by the id of the users.
 * @return a list of descriptions of all the users registered in the library
 */
  List<String> getUserDescriptions() {
    List<String> desc = new ArrayList<>();
    for (User user : getUserList()) { 
      desc.add(user.getDescription());
    }
    return List.copyOf(desc);
  }


/**
 * Register a user with given name and email.
 * @param userName the user's name
 * @param email the user's email
 * @return the registered user
 */
  public User registerUser(String userName, String email){
    User user = new User(_userId, userName, email);
    _userList.add(user);
    incrementUserIdLibrary();
    setDirty(true);
    return user;
  }

/**
 * Returns the user with the given id.
 * If there is no user with the given id, returns null.
 * @param idUser the id of the user to be retrieved
 * @return the user with the given id, or null if there's no user with the given id
 */
  User getUser(int idUser){
    for (User user : _userList){
      if (user.getUserId() == idUser)
      return user; 
    }
    return null;
  }


/**
 * Read text input file at the beginning of the program and populates the
 * the state of this library with the domain entities represented in the text file.
 * 
 * @param filename name of the text input file to process
 * @throws UnrecognizedEntryException if some entry is not correct
 * @throws IOException if there is an IO erro while processing the text file
 **/
  void importFile(String filename) 
  throws UnrecognizedEntryException, IOException {
    new MyParser(this).parseFile(filename);
    setDirty(true);
  }


/**
 * Calculates the deadline for a given work based on the total number of copies and the user's behavior.
 * 
 * @param work the work for which the deadline should be calculated
 * @param user the user whose behavior should be used to calculate the deadline
 * 
 * @return the deadline for the given work based on the user's behavior
 */
int calculateDeadline(Work work, User user) {
    int totalCopies = work.getTotalCopies(); 
    
    UserBehavior userBehavior = user.getUserBehavior();

    if (totalCopies == 1) {
        return userBehavior.getDeadlineForOneCopy();
        
    } else if (totalCopies <= 5 && totalCopies > 1) {
        return userBehavior.getDeadlineForFiveOrLessCopies();
        
    } else if (totalCopies > 5) {
        return userBehavior.getDeadlineForMoreThanFiveCopies();
    }
    return 0;
}

/**
 * Search for works whose description contains the given term.
 * @param term the term to search for
 * @return a list of descriptions of works whose description contains the given term
 */
public List<String> searchWorks(String term) {
  String q = term.toLowerCase();
  List<String> out = new ArrayList<>();
  for (Work w : getWorks()) {
    String desc = w.getDescription();
    if (desc != null && desc.toLowerCase().contains(q))
      out.add(desc);
  }
  return List.copyOf(out);
}


/**
 * Requests a work for a given user. First, it checks if the user is active and if not, it throws a BorrowingRuleFailedCoreException.
 * Then, it applies all the validation rules. If any rule fails, it throws a BorrowingRuleFailedCoreException.
 * Finally, it creates a new request and adds it to the user and work, decrementing the available copies of the work.
 * 
 * @param user the user making the request
 * @param work the work being requested
 * @return the deadline for the request
 * @throws NoSuchUserCoreException if the user does not exist
 * @throws NoSuchWorkCoreException if the work does not exist
 * @throws BorrowingRuleFailedCoreException if the user is not active or if any rule fails
 */
int requestWork(User user, Work work) 
throws BorrowingRuleFailedCoreException, WorkNotBorrowedByUserCoreException {
        _lastFailedRuleId = 0; // Reset the last failed rule id
        
        if (_allOpenRequests.size() >= 12) {
          throw new WorkNotBorrowedByUserCoreException(user.getUserId(), work.getWorkId()); 
      }

        if (user.hasOverdue(_currentDate) || user.getUserFine() > 0) 
          user.setActive(false);

        if (!user.isActive()) {
          _lastFailedRuleId = 2;
          throw new BorrowingRuleFailedCoreException(user.getUserId(),
            work.getWorkId(), 2);
        }
        for (Rule rule : _rules) {
            if (!rule.check(work, user)) {
                _lastFailedRuleId = rule.getId();
                throw new BorrowingRuleFailedCoreException(user.getUserId(),
                work.getWorkId(), rule.getId());
            }
        }
        int deadlineDays = calculateDeadline(work, user); 
        int absoluteDeadline = _currentDate + deadlineDays;

        Request newRequest = new Request(user, work);
        newRequest.setDeadline(absoluteDeadline); 
        
        user.addRequest(newRequest); 
        _allOpenRequests.add(newRequest);
        work.decrementAvailableCopies(); 
        work.clearInterestedFor(user);
        setDirty(true);
        
        return absoluteDeadline;
    }


/**
 * Returns a work previously borrowed by a user. First, it checks if the
 * user has an open request for the given work. If not, it throws a
 * WorkNotBorrowedByUserCoreException. Then, it updates the user and work
 * state, calculating a fine based on the difference between the current
 * date and the deadline of the request. If the fine is greater than 0, it
 * sets the user as inactive and updates their behavior if necessary.
 * 
 * @param user the user returning the work
 * @param work the work being returned
 * @return the fine calculated based on the difference between the current date and the deadline of the request
 * @throws WorkNotBorrowedByUserCoreException if the user does not have an open request for the given work
 */
  int returnWork(User user, Work work) 
  throws WorkNotBorrowedByUserCoreException {
      Request request = user.findOpenRequest(work); 
      
      if (request == null) {
          throw new WorkNotBorrowedByUserCoreException(work.getWorkId(),
          user.getUserId());
      }
      
      // Return is successful. Remove request.
      user.removeRequest(request); 
      work.incrementAvailableCopies(); 
      _allOpenRequests.remove(request);

      // Calculate fine
      int daysLate = Math.max(0, _currentDate - request.getDeadline());
      int fine = daysLate > 0 ? 5 * daysLate + user.getUserFine(): 0;
      user.addFine(fine);
      
      if (fine > 0) {
        user.setActive(false);
        if (user.getUserBehavior() == Cumpridor.getInstance()) {
          user.setUserBehavior(Normal.getInstance());
        }
      } 

      user.recordReturn(daysLate==0);
      setDirty(true);
      return fine;
  }
  


/**
 * Changes the total number of copies and the available number of copies of a work by a given delta.
 * 
 * @param workId the id of the work to change
 * @param delta the amount to change the total number of copies and the available number of copies
 * @return true if the change was successful, false if the new available number of copies would be negative or the new total number of copies would be less than the borrowed number of copies
 */
  boolean changeCopies(int workId, int delta) {
    Work work = getWork(workId);
    int avail = work.getAvailableCopies();
    int total = work.getTotalCopies();
    int borrowed = work.getBorrowedCount();
    int newAvail = avail + delta;
    int newTotal = total + delta;
    if (newAvail < 0|| newTotal < borrowed) return false;

    boolean wasZero = (avail == 0);
    work.setAvailableCopies(newAvail);
    work.setTotalCopies(newTotal);
    if (wasZero && newAvail > 0) work.notifyAvailability();
    setDirty(true);
    return true;
  }


  
  public List<User> getUsersWithFineGreaterThan(int amount) throws IllegalArgumentException {
      if (amount < 0) {
          throw new IllegalArgumentException("O valor da multa não pode ser negativo.");
      }
      
      List<User> matchingUsers = new ArrayList<>();
      for (User user : _userList) {
          if (user.getUserFine() >= amount) {
              matchingUsers.add(user);
          }
      }
      Collections.sort(matchingUsers,
       new Comparator<User>() {
          @Override
          public int compare(User u1, User u2) {
              return Integer.compare(u2.getUserFine(), u1.getUserFine());
          }
      });
      return matchingUsers; 
  }


  public User getUserWithHighestValue() {
      User bestUserSoFar = null;
      int maxValueSoFar = 0; 

      for (User currentUser : _userList) {
          int currentValue = currentUser.getTotalRequestedValue();
          if (currentValue == 0) {
              continue;
          }
          if (bestUserSoFar == null) {
              bestUserSoFar = currentUser;
              maxValueSoFar = currentValue;
          } 
          else if (currentValue > maxValueSoFar) {
              bestUserSoFar = currentUser;
              maxValueSoFar = currentValue;
          } 
          else if (currentValue == maxValueSoFar) {
              
              String currentName = currentUser.getUserName(); 
              String bestName = bestUserSoFar.getUserName();  

              if (currentName.length() < bestName.length()) {
                  bestUserSoFar = currentUser;
              }
          }
      }
      return bestUserSoFar;
  }
}