package bci.app.request;

import bci.core.LibraryManager;
import bci.app.exception.BorrowingRuleFailedException;
import bci.core.exception.WorkNotBorrowedByUserCoreException;
import bci.core.exception.BorrowingRuleFailedCoreException;
import bci.app.exception.NoSuchUserException;
import bci.core.exception.NoSuchUserCoreException;
import bci.app.exception.NoSuchWorkException;
import bci.core.exception.NoSuchWorkCoreException;
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.menus.CommandException;
import pt.tecnico.uilib.forms.Form;

public final class DoRequestWork extends Command<LibraryManager> {

  public DoRequestWork(LibraryManager receiver) {
    super(Label.REQUEST_WORK, receiver);
    
  }

  @Override
  public void execute() throws CommandException {
      int _userId = Form.requestInteger("Introduza o número de utente: ");
      int _workId = Form.requestInteger("Introduza o número da obra: ");
     
      try {
        int deadline = _receiver.requestWork(_userId, _workId);
        _display.addLine(Message.workReturnDay(_workId, deadline));
        } catch (NoSuchUserCoreException e) {
          throw new NoSuchUserException(_userId); 
        } catch (NoSuchWorkCoreException e){
          throw new NoSuchWorkException(_workId);
        }catch (BorrowingRuleFailedCoreException | WorkNotBorrowedByUserCoreException e) {
          if (_receiver.getLastFailedRuleId() == 3){
          String response = Form.requestString(Prompt.returnNotificationPreference());
            if ("s".equalsIgnoreCase(response)) { 
                _receiver.registerAvailabilityInterest(_userId, _workId);
            }
          } else {
            throw new BorrowingRuleFailedException(_userId, _workId, _receiver.getLastFailedRuleId()); 
          }
      }
    _display.display();
  }

}

