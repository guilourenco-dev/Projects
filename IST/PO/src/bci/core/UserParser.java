package bci.core;

import bci.core.exception.UnrecognizedEntryException;


public class UserParser implements EntryParser {
    private final Library _library;

    public UserParser(Library library) {
        _library = library;
    }
    @Override
    public boolean handlesType(String type) {
        return "USER".equals(type);
    }
    @Override
    public void parse(String[] components, String line) 
    throws UnrecognizedEntryException{
        if (components.length != 3)
            throw new UnrecognizedEntryException
            ("Número inválido de campos (3) na descrição de um utente: " 
            + line);
        String name = components[1];
        String email = components[2];
        _library.registerUser(name, email);
    }
}
