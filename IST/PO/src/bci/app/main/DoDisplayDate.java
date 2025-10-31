package bci.app.main;

import bci.core.LibraryManager;
import pt.tecnico.uilib.menus.Command;

class DoDisplayDate extends Command<LibraryManager> {

  DoDisplayDate(LibraryManager receiver) {
    super(Label.DISPLAY_DATE, receiver);
  }

  @Override
  protected final void execute() {
    int d = _receiver.getCurrentDate();
    _display.addLine(Message.currentDate(d));
    _display.display();                       
  }

}
