package bci.app.work;

import bci.core.LibraryManager;
import bci.app.exception.NoSuchCreatorException;
import pt.tecnico.uilib.forms.Form;
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.menus.CommandException;

class DoDisplayWorksByCreator extends Command<LibraryManager> {
  DoDisplayWorksByCreator(LibraryManager receiver) {
    super(Label.SHOW_WORKS_BY_CREATOR, receiver);
  }

  @Override
  protected final void execute() throws CommandException{
    String creatorId = Form.requestString(Prompt.creatorId());
    if (!_receiver.findCreator(creatorId))
      throw new NoSuchCreatorException(creatorId);
    for (var w : _receiver.getWorksByCreator(creatorId)) 
      _display.addLine(w.getDescription());
    _display.display();
  }
}

