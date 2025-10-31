package bci.core;

public class Book extends Work {
  private final String _isbn;
  private static final long serialVersionUID = 1L;
  
  public Book(int id, int price, int numOfCopies, String title, 
    Creator[] creator, String isbn, Category category) {
    super(id, price, numOfCopies, title, creator, category);
    _isbn = isbn;
  }

  protected String isbn() {return _isbn;}

  @Override
  public String toString() {         
    return "BOOK: " + getDescription();
  }


/**
 * Returns the type of the Work as a String.
 * @return "Livro"
 */
  @Override
  protected String getType() {
    return "Livro";
  }


/**
 * Returns a string with the names of all the creators of the book.
 * If the book has more than one creator, the names are separated by a semicolon.
 * @return a string with the names of the creators
 */
  protected String creatorNamesToString() {
    String message = "";
    Creator[] creator = getCreator();
    if (creator.length > 1){
      for (int i = 0; i < creator.length - 1; i++) {
        message += creator[i].getName() + "; ";
      }
      return message + creator[creator.length - 1].getName(); 
    } 
    return "" + creator[0].getName();  
  }
  

/**
 * Returns a string with additional information about this Book work.
 * The string has the format "creator - isbn" where creator is 
 * the name of the creator(s) of the work,
 * @return a string with additional information about this Book work
 */
  @Override
  protected String getAditionalInfo() {
    return String.format("%s - %s", creatorNamesToString(), _isbn);
  }


/**
 * Converts the given category to a string.
 * @param category the category to be converted
 * @return "Referência" for Category.REFERENCE,
 * "Ficção" for Category.FICTION, "Técnica e Científica" for Category.SCITECH,
 * and null for any other category.
 */
  @Override
  protected String categoryToString(Category category) {
    if (category == null) return null;
    return category.toString();
  }
}