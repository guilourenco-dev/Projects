package bci.core;

import bci.core.exception.UnrecognizedEntryException;

public class DvdParser implements EntryParser{
    private final Library _library;
    
    public DvdParser(Library library) {
    _library = library;
    }
    
    @Override
    public boolean handlesType(String type) {
      return "DVD".equals(type);
    }
    
    @Override
    public void parse(String[] components, String line) 
    throws UnrecognizedEntryException {
    if (components.length != 7){
      throw new UnrecognizedEntryException
      ("Número inválido de campos (7) na descrição de um DVD: " + line);
    }
    int id = _library.getNextWorkId();
    String title = components[1];
    Creator[] crs = { _library.registerCreator(components[2].trim()) }; // array com 1 criador
    int price = _library.parseInt(components[3], "price", line);

    Category category;
    try {
        category = Category.valueOf(components[4].toUpperCase());
    } catch (IllegalArgumentException e) {
        throw new UnrecognizedEntryException
        ("Categoria inválida na descrição de um DVD: " + line, e);
    }
    String igac    = components[5];
    int numOfCopies  = _library.parseInt(components[6], "copies", line);
    _library.registerDvd( id, price, numOfCopies, title, crs, category, igac);
  }
}