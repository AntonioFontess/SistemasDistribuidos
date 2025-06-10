package hotel.rmi;

import java.rmi.Naming;
import java.util.List;
import java.util.Scanner;

public class ClienteHotel {
    public static void main(String[] args) {
        try {
            GerenciadorQuartos hotel = (GerenciadorQuartos) Naming.lookup("rmi://localhost:1099/HotelService");
            Scanner scanner = new Scanner(System.in);
            String opcao;

            do {
                System.out.println("\n--- MENU ---");
                System.out.println("1 - Listar quartos disponiveis");
                System.out.println("2 - Fazer reserva");
                System.out.println("3 - Listar hospedes");
                System.out.println("0 - Sair");
                System.out.print("Escolha uma opçao: ");
                opcao = scanner.nextLine();

                switch (opcao) {
                    case "1":
                        System.out.println(hotel.listagem());
                        break;
                    case "2":
                        System.out.print("Informe o tipo de quarto (0 a 4): ");
                        int tipo = Integer.parseInt(scanner.nextLine());
                        System.out.print("Informe o nome do hospede: ");
                        String nome = scanner.nextLine();
                        System.out.println(hotel.reserva(tipo, nome));
                        break;
                    case "3":
                        List<String> lista = hotel.hospedes();
                        System.out.println("Hospedes:");
                        for (String h : lista) {
                            System.out.println(" - " + h);
                        }
                        break;
                    case "0":
                        System.out.println("Saindo...");
                        break;
                    default:
                        System.out.println("Opçao invalida.");
                }

            } while (!opcao.equals("0"));

            scanner.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

