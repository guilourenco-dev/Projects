package bci.core;

public final class Dvd extends Work {
  
  private final String _igac;
  private static final long serialVersionUID = 1L;
  
  public Dvd(int id, int price, int numOfCopies, String title, 
  Creator[] creator, String igac, Category category) {
    super(id, price, numOfCopies, title, creator, category);
    _igac = igac;
  }

  @Override
  public String toString() {
    return "DVD: " + getDescription();
  }

/**
 * Returns the type of this work.
 * @return "DVD" for a DVD work.
 */
  @Override
  protected String getType() {
    return "DVD";
  }

/**
 * Returns a string with additional information about this DVD work.
 * The string has the format "creator - igac" where creator is the name of the only creator of the work,
 * and igac is the IGAC number of the work.
 * @return a string with additional information about this DVD work
 */
  @Override
  protected String getAditionalInfo() {
    return String.format("%s - %s", getCreator()[0].getName(), _igac);
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