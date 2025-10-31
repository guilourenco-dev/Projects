package bci.app.user;

import bci.core.LibraryManager;
import bci.core.User; 
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.menus.CommandException;

class DoShowUserWithHighestValue extends Command<LibraryManager> {
  DoShowUserWithHighestValue(LibraryManager receiver) {
    super("Utente com maior valor", receiver); 
  }


  @Override
  protected final void execute() throws CommandException {
    
    User winner = _receiver.getUserWithHighestValue();
    if (winner == null) {
        _display.addLine("Sem obras");
    } else {
        int maxValue = winner.getTotalRequestedValue();  
        _display.addLine(winner.getUserId() + " - " + maxValue); 
    }
    _display.display();
  }
}