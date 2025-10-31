package bci.core;

import java.util.Collection;
import java.util.Arrays;
import java.util.ArrayList;
import java.io.Serializable;


public class Creator implements Serializable{
    private static final long serialVersionUID = 202508101409L; 
    private final String _name;
    private Work[] _works; 
    private final int _id;
    
    public Creator(int id, String name){ 
        _id = id;
        _name = name; 
        _works = new Work[0];
    }

    String getName(){return _name;}
    protected int getId(){return _id;} 

    protected void add(Work work){
        if (work == null) return;
        for (Work wrk : _works) if (wrk == work) return;
        Work[] newWork = Arrays.copyOf(_works, _works.length + 1);
        newWork[_works.length] = work;
        _works = newWork;
    }

    protected void remove(Work work){
        if (work == null || _works.length == 0) return;
    ArrayList<Work> list = new ArrayList<>(Arrays.asList(_works));
    if (list.remove(work)) 
        _works = list.toArray(new Work[0]);
    }

    protected Collection<Work> works(){
        return new ArrayList<>(Arrays.asList(_works));
    }
}