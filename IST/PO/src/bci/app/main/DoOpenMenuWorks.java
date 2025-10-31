package bci.app.main;

import bci.core.LibraryManager;
import pt.tecnico.uilib.menus.Command;
import bci.app.work.Menu;
class DoOpenMenuWorks extends Command<LibraryManager> {

  DoOpenMenuWorks(LibraryManager receiver) {
    super(Label.OPEN_MENU_WORKS, receiver);
  }

  @Override
  protected final void execute() {
    try { 
    new Menu(_receiver).open(); // abrir o menu de obras
    _display.addNewLine("1 - Mostrar obra", true);
    _display.addNewLine("2 - Mostrar todas as obras", true);
    _display.addNewLine("3 - Efectuar pesquisa de termos", true);
    _display.addNewLine("4 - Mostrar todas as obras de um criador", true);
    _display.addNewLine("5 - Alterar inventário de uma obra", true);
    _display.addNewLine("0 - Sair", true);
    _display.clear();
    } catch (Exception e) { //Evitar apanhar excepÃ§Ãµes demasiado genÃ©ricas (RuntimeException and Exception) em blocos try-catch.
      _display.addLine(e.getMessage());
    }
  }
}
