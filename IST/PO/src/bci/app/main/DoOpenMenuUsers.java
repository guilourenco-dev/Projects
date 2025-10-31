package bci.app.main;

import bci.core.LibraryManager;
import pt.tecnico.uilib.menus.Command;
import bci.app.user.Menu; // importar o menu de users

class DoOpenMenuUsers extends Command<LibraryManager> {

  DoOpenMenuUsers(LibraryManager receiver) {
    super(Label.OPEN_MENU_USERS, receiver); 
  }

  @Override
  protected final void execute() {
    try {
      new Menu(_receiver).open(); // abrir o menu de users
      _display.addNewLine("1 - Registar utente", false);
      _display.addNewLine("2 - Mostrar utente", false);
      _display.addNewLine("3 - Listar utentes", false);
      _display.addNewLine("4 - Mostrar notificações de utente", false);
      _display.addNewLine("5 - Saldar multa de utente", false);
      _display.addNewLine("0 - Sair", false);
      _display.clear();
    } catch (Exception e) { //Evitar apanhar excepÃ§Ãµes demasiado genÃ©ricas (RuntimeException and Exception) em blocos try-catch.
      System.err.println("Error opening menu: " + e.getMessage());
    }
  } 
}
