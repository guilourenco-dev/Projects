package bci.app.user;

import bci.core.LibraryManager;
import bci.core.User; 
import pt.tecnico.uilib.forms.Form;
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.menus.CommandException;
import java.util.List;

class DoShowUsersWithFineGreaterThan extends Command<LibraryManager> {
  DoShowUsersWithFineGreaterThan(LibraryManager receiver) {
    super("Apresenta utentes com dívida maior", receiver); 
  }
 
  @Override
  protected final void execute() throws CommandException {

    int minValue = Form.requestInteger(Prompt.userId()); 

    List<User> _usersList = _receiver.getUsersWithFineGreaterThan(minValue);
    _display.addLine("Número de utentes: " + _usersList.size());
    for (User user : _usersList) {
      _display.addLine(user.getUserFine() + " - " + user.getUserName()); 
    }
    _display.display();
  }
}