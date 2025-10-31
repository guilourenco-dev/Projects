package bci.core;

import java.io.Serializable;

public class Date extends Library implements Serializable {
    private int _currentDate;
    private static final long serialVersionUID = 202508101411L;

    // Constructor
    public Date(){
        // Empty
    }

    @Override
    public int getCurrentDate(){ return _currentDate;} // retorna a data atual


    /**
     * Advances the library's current date by the given number of days.
     * @param nDays the number of days to advance
     */
    @Override
    public  void advanceDays(int nDays){
        if (nDays<=0) return;
        _currentDate += nDays;
    }
}
