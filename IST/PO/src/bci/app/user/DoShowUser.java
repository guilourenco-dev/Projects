package bci.app.user;

import bci.core.LibraryManager;
import bci.app.exception.NoSuchUserException;
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.menus.CommandException;
import pt.tecnico.uilib.forms.Form;

class DoShowUser extends Command<LibraryManager> {

  DoShowUser(LibraryManager receiver) {
    super(Label.SHOW_USER, receiver);
  }
  
  @Override
  protected final void execute() throws CommandException { 
    int idUser = Form.requestInteger(Prompt.userId());
    if (!_receiver.findUser(idUser)){
      throw new NoSuchUserException(idUser);
    }
    _display.addLine(_receiver.getUserDescription(idUser));
    _display.display();
    _display.clear();
  }
}