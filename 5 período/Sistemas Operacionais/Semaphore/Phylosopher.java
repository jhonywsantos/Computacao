package Semaphore;

import java.util.concurrent.Semaphore;


public class Phylosopher extends Thread{
    private int id;
    private Semaphore hashiEsquerdo;
    private Semaphore hashiDireito;

    public Phylosopher(int id, Semaphore hashiEsquerdo, Semaphore hashiDireito) {
        this.id = id;
        this.hashiEsquerdo = hashiEsquerdo;
        this.hashiDireito = hashiDireito;
    }
    private void think() throws InterruptedException {
        System.out.println("Phylosopher " + id + " is thinking.");
        Thread.sleep((long) (Math.random() * 1000));
    }

        private void eat() throws InterruptedException {
        System.out.println("Filósofo " + id + " está comendo...");
        Thread.sleep((long) (Math.random() * 2000));
    }
    public void run() {
        try {
            while (true) {
                think();
                hashiEsquerdo.acquire();
                hashiDireito.acquire();
                eat();
                hashiDireito.release();
                hashiEsquerdo.release();
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}