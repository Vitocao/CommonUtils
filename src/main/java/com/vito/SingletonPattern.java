package com.vito;

public class SingletonPattern {

    //避免指令重排
    //非原子性操作有指令重排问题

    private static volatile SingletonPattern instance;

    private SingletonPattern() {}

    public static SingletonPattern getInstance(){
        //双重校验+同步锁
        if(instance == null){
            synchronized (SingletonPattern.class){
                if (instance == null){
                    instance = new SingletonPattern();
                }
            }
        }
        return instance;
    }
}
