package bci.core;

import bci.core.exception.UnrecognizedEntryException;


public class BookParser implements EntryParser{
    private final Library _library;
    
    public BookParser(Library library) {
    _library = library;
    }
    
    @Override
    public boolean handlesType(String type) {
        return "BOOK".equals(type);
    }
    
    @Override
    public void parse(String[] components, String line)
    throws UnrecognizedEntryException {    
        if (components.length != 7){
            throw new UnrecognizedEntryException
        ("Número inválido de campos (7) na descrição de um Book: " + line);
        }
        int id = _library.getNextWorkId();
        String title   = components[1];
        String[] names = components[2].split(",");
        Creator[] crs  = new Creator[names.length];
        for (int i = 0; i < names.length; i++){
            crs[i] = _library.registerCreator(names[i].trim());
        }
        int price = _library.parseInt(components[3], "price", line);
        Category category;
        try {
            category = Category.valueOf(components[4].toUpperCase());
        } catch (IllegalArgumentException e) {
            throw new UnrecognizedEntryException
        ("Categoria inválida na descrição de um BOOK: " + line, e);
        }        
        String isbn = components[5];
        int numOfCopies = _library.parseInt(components[6], "copies", line);

        _library.registerBook
        (id, price , numOfCopies, title, crs, category, isbn);
    }
}