package bci.app.work;

import bci.core.LibraryManager;
import pt.tecnico.uilib.menus.Command;

/**
 * Command to display all works.
 */
class DoDisplayWorks extends Command<LibraryManager> {

  DoDisplayWorks(LibraryManager receiver) {
    super(Label.SHOW_WORKS, receiver);
  }

  @Override
  protected final void execute() {
    for (String des: _receiver.getWorkDescriptions()) { 
      _display.addLine(des); 
    }
    _display.display();
  }
}
