package bci.app.request;

import bci.core.LibraryManager;
import bci.app.exception.NoSuchUserException;
import bci.core.exception.NoSuchUserCoreException;
import bci.app.exception.NoSuchWorkException;
import bci.core.exception.NoSuchWorkCoreException;
import bci.app.exception.WorkNotBorrowedByUserException;
import bci.core.exception.WorkNotBorrowedByUserCoreException;
import bci.app.exception.UserIsActiveException;
import bci.core.exception.UserIsActiveCoreException;
import pt.tecnico.uilib.forms.Form;
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.menus.CommandException;
//FIXME add more imports if needed

/**
 * 4.4.2. Return a work.
 */
class DoReturnWork extends Command<LibraryManager> {

  DoReturnWork(LibraryManager receiver) {
    super(Label.RETURN_WORK, receiver);
    //FIXME add command fields
  }

  @Override
  protected final void execute() throws CommandException {
    int _userId = Form.requestInteger("Introduza o número de utente: ");
    int _workId = Form.requestInteger("Introduza o número da obra: ");
    
    try {

      int _fine = _receiver.returnWork(_userId, _workId);

      if (_fine > 0) {
          
          _display.addLine(Message.showFine(_userId, _fine));
            _display.display();
                    
          String response = Form.requestString(Prompt.finePaymentChoice()); 
          
          if ("s".equalsIgnoreCase(response)) {
            _receiver.payFine(_userId); 
          }
      }
    } catch (NoSuchUserCoreException e) {
        throw new NoSuchUserException(_userId);
    } catch (NoSuchWorkCoreException e) {
        throw new NoSuchWorkException(_workId);
    } catch (WorkNotBorrowedByUserCoreException e) {
        throw new WorkNotBorrowedByUserException(_workId, _userId);
    } catch (UserIsActiveCoreException e) {
        throw new UserIsActiveException(_userId);
    }

  }
}
