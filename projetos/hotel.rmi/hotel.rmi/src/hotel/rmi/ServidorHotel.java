package hotel.rmi;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class ServidorHotel {
    public static void main(String[] args) {
        try {
            LocateRegistry.createRegistry(1099);
            GerenciadorQuartos gerenciador = new GerenciadorQuartosImpl();
            Naming.rebind("rmi://localhost:1099/HotelService", gerenciador);
            System.out.println("Servidor de Hotel pronto.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
