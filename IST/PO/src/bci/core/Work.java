package bci.core;

import java.io.Serializable;
import java.util.LinkedHashSet;
import java.util.Set;


public abstract class Work implements Serializable, Comparable<Work> {

  private static final long serialVersionUID = 202508101410L;
  private final int _id; 
  private final String _title;
  private final Creator[] _creator; 
  private int _availableCopies;
  private int _totalCopies;
  private final int _price;
  private final Category _category;
  protected int _available;    
  private final Set<User> _waitlist = new LinkedHashSet<>();    

  // Constructor
  protected Work(int id, int price, int availableCopies, String title, Creator[] creator, Category category) {
    _id = id; 
    _price = price;
    _availableCopies = _totalCopies = availableCopies;
    _title = title; 
    _creator = creator;
    _category = category;
  }

  protected int getWorkId() { return _id; }
  protected String getTitle() { return _title; }
  protected Creator[] getCreator() { return _creator; }
  protected Category getCategory() { return _category; }

  public int getTotalCopies() { return _totalCopies; }
  public int getAvailableCopies()   { return _availableCopies; }
  public boolean isReference() { return _category == Category.REFERENCE; }
  public int getPrice() { return _price; }

  public void setTotalCopies(int v) { _totalCopies = v; }
  public int  getBorrowedCount()   { return _totalCopies - _availableCopies; }
  

/**
 * Compares this work to another work based on their ids.
 * @param work the work to compare to
 * @return a negative integer, zero, or a positive integer 
 * as this work's id is less than, equal to, or greater 
 * than the given work's id.
 */
  @Override 
  public int compareTo(Work work) { return Integer.compare(this.getWorkId(), work.getWorkId()); } 


  @Override 
  public abstract String toString(); // Abstract method to be implemented by subclasses
   
  protected abstract String getType(); // Abstract method to be implemented by subclasses
  
  protected abstract String getAditionalInfo(); // Abstract method to be implemented by subclasses

  protected abstract String categoryToString(Category category); // Abstract method to be implemented by subclasses  

/**
 * Returns a string with the work's information in the format:
 * id - n of t - type - title - price - category - additional info
 * where n is the number of copies of the work, t is the total number of copies,
 * type is the type of the work, title is the work's title, price is the work's price,
 * category is the work's category, and additional info is the work's additional information.
 * @return a string with the work's information
 */
  public  String getDescription(){
    return String.format("%d - %d de %d - %s - %s - %d - %s - %s", _id,
     _availableCopies, _totalCopies, getType(), _title, _price, 
    categoryToString(_category), getAditionalInfo());
  }

  void addInterested(User u) { _waitlist.add(u); }
void clearInterestedFor(User u) { _waitlist.remove(u); }
public boolean wasUnavailable() { return _availableCopies == 0; }

public void notifyAvailability() {
  String msg = "DISPONIBILIDADE: " + getDescription();
  for (User u : _waitlist) {
    u.addNotification(new Notification(msg));
  }
}

// ajustar increment/decrement existentes
  public void decrementAvailableCopies() { _availableCopies--; }
  public void incrementAvailableCopies() {
    boolean zero = (_availableCopies == 0);
    _availableCopies++;
    if (zero && _availableCopies > 0) notifyAvailability();
  }

  public void setAvailableCopies(int v){ _availableCopies = v; }

 

}
