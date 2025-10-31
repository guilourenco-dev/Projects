package bci.app.user;

import bci.core.LibraryManager;
import bci.app.exception.NoSuchUserException;
import bci.core.exception.NoSuchUserCoreException;
import bci.app.exception.UserIsActiveException;
import bci.core.exception.UserIsActiveCoreException;
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.menus.CommandException;
import pt.tecnico.uilib.forms.Form;

/**
 * 4.2.5. Settle a fine.
 */
class DoPayFine extends Command<LibraryManager> {

  DoPayFine(LibraryManager receiver) {
    super(Label.PAY_FINE, receiver);
    //FIXME add command fields
  }

  @Override
  protected final void execute() throws CommandException {
    int _userId = 0;
    try {
    _userId = Integer.parseInt(Form.requestString(Prompt.userId()));
    _receiver.payFine(_userId);  
    } catch (NoSuchUserCoreException e) {
      throw new NoSuchUserException(_userId);
    } catch (UserIsActiveCoreException e) {
      throw new UserIsActiveException(_userId);
    }
  }
}
