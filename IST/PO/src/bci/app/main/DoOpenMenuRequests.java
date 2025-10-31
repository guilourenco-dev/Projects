package bci.app.main;

import bci.core.LibraryManager;
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.menus.CommandException;
import bci.app.request.Menu;

class DoOpenMenuRequests extends Command<LibraryManager> {

  DoOpenMenuRequests(LibraryManager receiver) {
    super(Label.OPEN_MENU_REQUESTS, receiver);
  }

/**
 * Opens the requests menu.
 * 
 * <p>This command opens the requests menu where the user can request a work or return a work.</p>
 * 
 * <p>It shows the available options to the user and waits for its choice.</p>
 * 
 * @throws CommandException if some error occurs while executing the command.
 */
  @Override
  protected final void execute() throws CommandException {
    try { new Menu(_receiver).open(); 
    _display.addNewLine("1 - Requisitar obra", false);
    _display.addNewLine("2 - Devolver obra", false);
    _display.addNewLine("0 - Sair", false);
    _display.clear();
    } catch (Exception e) { // Evitar apanhar excepÃ§Ãµes demasiado genÃ©ricas (RuntimeException and Exception) em blocos try-catch.
      _display.addLine(e.getMessage());
    }
  }
}
