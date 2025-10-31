package bci.app.main;

import bci.core.LibraryManager;
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.forms.Form; 
import pt.tecnico.uilib.menus.CommandException;

class DoAdvanceDate extends Command<LibraryManager> {
  DoAdvanceDate(LibraryManager receiver) {
    super(Label.ADVANCE_DATE, receiver);
    
  }

  @Override
  protected final void execute() throws CommandException{
    int days = Form.requestInteger(Prompt.daysToAdvance()); 
    if (days <= 0) return;  
    _receiver.advanceDays(days); 
    _display.display();
  }
}
