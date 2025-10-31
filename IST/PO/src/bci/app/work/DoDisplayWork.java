package bci.app.work;

import bci.core.LibraryManager;
import bci.app.exception.NoSuchWorkException;
import pt.tecnico.uilib.forms.Form;
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.menus.CommandException;

/**
 * Command to display a work.
 */
class DoDisplayWork extends Command<LibraryManager> {

  DoDisplayWork(LibraryManager receiver) {
    super(Label.SHOW_WORK, receiver);

  }

  @Override
  protected final void execute() throws CommandException { 
    int _id = Form.requestInteger(Prompt.workId());
    if (!_receiver.findWork(_id))
      throw new NoSuchWorkException(_id);
    String work = _receiver.getWorkDescription(_id);               
    _display.addLine(work); 
  }
} 
