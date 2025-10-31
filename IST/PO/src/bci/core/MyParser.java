package bci.core;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;

import bci.core.exception.UnrecognizedEntryException;

class MyParser {
  private final List<EntryParser> parsers; 

  // Constructor
  MyParser(Library lib) {
    parsers = List.of(new UserParser(lib), new DvdParser(lib), new BookParser(lib));
  }
  

  /**
   * Parse a text file and populate the state of the library with the domain entities
   * represented in the text file.
   * 
   * @param filename name of the text file to process
   * @throws IOException if there is an IO erro while processing the text file
   * @throws UnrecognizedEntryException if some entry is not correct
   */
  void parseFile(String filename) throws IOException, UnrecognizedEntryException {
    try (BufferedReader input = new BufferedReader(new FileReader(filename))) {
      String line;
      int ln = 0;
      while ((line = input.readLine()) != null) {
        ln++;
        line = line.trim();
        if (line.isEmpty() || line.startsWith("#")) continue;
        try {
          parseLine(line);
        } catch (UnrecognizedEntryException e) {
          // anexa nº da linha para debug
          throw new UnrecognizedEntryException("linha " + ln + ": " + line, e);
        }
      }
    }
  }

  private void parseLine(String line) throws UnrecognizedEntryException {
        String[] components = line.split(":");
        String entryType = components[0];

        // Usa polimorfismo para encontrar o parser correto.
        for (EntryParser parser : parsers) {
            if (parser.handlesType(entryType)) {
                parser.parse(components, line);
                return; // Encontrou e processou, sai
            }
        }
        
        // Se nenhum parser lidar com o tipo, lança exceção.
        throw new UnrecognizedEntryException("Tipo inválido " + entryType + " na linha " + line);
    }
}
