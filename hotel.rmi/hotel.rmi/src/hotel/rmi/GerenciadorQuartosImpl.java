package hotel.rmi;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.*;

public class GerenciadorQuartosImpl extends UnicastRemoteObject implements GerenciadorQuartos {

    private final Map<Integer, Integer> totalQuartos;
    private final Map<Integer, Integer> quartosDisponiveis;
    private final Map<Integer, Double> precos;
    private final List<String> nomesHospedes;

    public GerenciadorQuartosImpl() throws RemoteException {
        totalQuartos = Map.of(
            0, 10,
            1, 20,
            2, 5,
            3, 3,
            4, 2
        );

        precos = Map.of(
            0, 100.0,
            1, 150.0,
            2, 200.0,
            3, 250.0,
            4, 300.0
        );

        quartosDisponiveis = new HashMap<>();
        for (int tipo : totalQuartos.keySet()) {
            quartosDisponiveis.put(tipo, totalQuartos.get(tipo));
        }

        nomesHospedes = new ArrayList<>();
    }

    public synchronized String listagem() throws RemoteException {
        StringBuilder sb = new StringBuilder("Quartos disponiveis:\n");
        for (int tipo : totalQuartos.keySet()) {
            sb.append(String.format("Tipo %d - R$ %.2f - %d disponiveis\n",
                    tipo, precos.get(tipo), quartosDisponiveis.get(tipo)));
        }
        return sb.toString();
    }

    public synchronized String reserva(int tipo, String nome) throws RemoteException {
        if (!quartosDisponiveis.containsKey(tipo)) {
            return "Tipo de quarto invalido.";
        }

        if (quartosDisponiveis.get(tipo) > 0) {
            quartosDisponiveis.put(tipo, quartosDisponiveis.get(tipo) - 1);
            nomesHospedes.add(nome + " (Tipo " + tipo + ")");
            return "Reserva realizada com sucesso para " + nome + " no quarto tipo " + tipo;
        } else {
            return "Nao ha quartos disponiveis do tipo " + tipo;
        }
    }

    public synchronized List<String> hospedes() throws RemoteException {
        return new ArrayList<>(nomesHospedes);
    }
}
