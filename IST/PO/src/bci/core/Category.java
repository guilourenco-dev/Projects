package bci.core;

public enum Category {
    REFERENCE("Referência"), 
    FICTION("Ficção"), 
    SCITECH("Técnica e Científica"); 
    private final String displayString;

    private Category(String displayString) {
        this.displayString = displayString;
    }

    @Override
    // Método que retorna a representação da categoria
    public String toString() {
        return displayString; // Polimorfismo
    }
}