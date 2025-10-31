package bci.core.parser;

import bci.core.exception.UnrecognizedEntryException;

public interface EntryParser {
    // Verifica se este parser pode lidar com a entrada
    boolean handlesType(String type); 
    // Executa a lógica de parsing
    void parse(String[] components, String line) 
    throws UnrecognizedEntryException;
}
