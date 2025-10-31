package bci.app.user;

import bci.core.LibraryManager;
import bci.app.exception.NoSuchUserException;
import bci.core.exception.NoSuchUserCoreException;
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.menus.CommandException;
import pt.tecnico.uilib.forms.Form;
/**
 * 4.2.3. Show notifications of a specific user.
 */
class DoShowUserNotifications extends Command<LibraryManager> {

  DoShowUserNotifications(LibraryManager receiver) {
    super(Label.SHOW_USER_NOTIFICATIONS, receiver);
    //FIXME add command fields
  }

  @Override
  protected final void execute() throws CommandException {
    int _userId = Integer.parseInt(Form.requestString(Prompt.userId()));
    try {
      for (String s : _receiver.consumeUserNotifications(_userId)){
        _display.addLine(s);
      }
      _display.display();
    } catch (NoSuchUserCoreException e) { 
      throw new NoSuchUserException(_userId); }
  }
}
