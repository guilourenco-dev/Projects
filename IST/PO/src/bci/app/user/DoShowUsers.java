package bci.app.user;

import bci.core.LibraryManager;
import pt.tecnico.uilib.menus.Command;
import java.util.ArrayList;
import java.util.List;

class DoShowUsers extends Command<LibraryManager> {
  DoShowUsers(LibraryManager receiver) {
    super(Label.SHOW_USERS, receiver);
  }

 @Override
  protected final void execute() {
    _display.clear();

    List<String> sortedUsersList = new ArrayList<>(_receiver.getUserDescriptions());

    sortedUsersList.sort((userString1, userString2) -> {
      String name1 = userString1.split(" - ")[1];
      String name2 = userString2.split(" - ")[1];
      return name1.compareToIgnoreCase(name2);
  });
    for (String s : sortedUsersList) {
      _display.addLine(s);
    }

    _display.display();
  }
}