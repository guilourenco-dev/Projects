package bci.app.work;

import bci.core.LibraryManager;
import bci.app.exception.NoSuchWorkException;
import bci.core.exception.NoSuchWorkCoreException;
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.menus.CommandException;
import pt.tecnico.uilib.forms.Form;

/**
 * Change the number of exemplars of a work.
 */
class DoChangeWorkInventory extends Command<LibraryManager> {
  DoChangeWorkInventory(LibraryManager receiver) {
    super(Label.CHANGE_WORK_INVENTORY, receiver);
     //FIXME add command fields
  }

  @Override
  protected final void execute() throws CommandException {
    int workId = Form.requestInteger(Prompt.workId());
    int delta = Form.requestInteger(Prompt.amountToDecrement()); 
    try {
      boolean ok = _receiver.changeCopies(workId, delta);
      if (!ok) _display.addLine(Message.notEnoughInventory(workId, delta));
      _display.display();
    } catch (NoSuchWorkCoreException e) { 
      throw new NoSuchWorkException(workId); }
  }
}
 
