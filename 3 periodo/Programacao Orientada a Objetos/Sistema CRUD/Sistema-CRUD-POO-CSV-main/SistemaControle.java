import java.io.*;
import java.util.*;

class Usuario {
    private String nome;
    private double altura;
    private String sexo;
    private double peso;
    private String username;
    private String senha;
    private double imc;
    private String statusImc;

    public Usuario(String nome, double altura, String sexo, double peso, String username, String senha) {
        this.nome = nome;
        this.altura = altura;
        this.sexo = sexo;
        this.peso = peso;
        this.username = username;
        this.senha = senha;
        this.imc = calcularImc();
        this.statusImc = verificarStatusImc();
    }

    public double calcularImc() {
        return peso / (altura * altura);
    }

    public String verificarStatusImc() {
        if (imc >= 17 && imc <= 18.5) {
            return "Status: Abaixo do peso";
        } else if (imc > 18.5 && imc <= 24.99) {
            return "Status: Peso ideal";
        } else if (imc >= 25 && imc <= 29.99) {
            return "Status: Sobrepeso";
        } else if (imc >= 30) {
            return "Status: Obesidade";
        } else {
            return "IMC fora do alcance esperado";
        }
    }

    public String getUsername() {
        return username;
    }

    public String getSenha() {
        return senha;
    }

    public String[] toCsvRow() {
        return new String[]{nome, String.valueOf(altura), sexo, String.valueOf(peso), username, senha, String.format("%.2f", imc), statusImc};
    }
}

public class SistemaControle {
    private static final String CSV_FILE = "FichaUsuario.csv";

    public static Usuario recolherInformacoesUsuario() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite seu nome: ");
        String nome = scanner.nextLine();

        double altura = 0;
        while (true) {
            System.out.print("Digite sua altura em metros (ex: 1.75): ");
            try {
                altura = Double.parseDouble(scanner.nextLine().replace(',', '.'));
                break;
            } catch (NumberFormatException e) {
                System.out.println("Entrada inválida. Por favor, digite um número válido para a altura.");
            }
        }

        System.out.print("Digite seu sexo (M/F): ");
        String sexo = scanner.nextLine();

        double peso = 0;
        while (true) {
            System.out.print("Digite seu peso em kg: ");
            try {
                peso = Double.parseDouble(scanner.nextLine().replace(',', '.'));
                break;
            } catch (NumberFormatException e) {
                System.out.println("Entrada inválida. Por favor, digite um número válido para o peso.");
            }
        }

        String username;
        while (true) {
            System.out.print("Escolha um nome de usuário: ");
            username = scanner.nextLine();
            if (usuarioExiste(username)) {
                System.out.println("Nome de usuário já cadastrado! Por favor, insira um nome válido.");
            } else {
                break;
            }
        }

        System.out.print("Escolha uma senha: ");
        String senha = scanner.nextLine();

        return new Usuario(nome, altura, sexo, peso, username, senha);
    }

    public static boolean usuarioExiste(String username) {
        try (BufferedReader br = new BufferedReader(new FileReader(CSV_FILE))) {
            String linha;
            while ((linha = br.readLine()) != null) {
                String[] data = linha.split(",");
                if (data.length >= 5 && data[4].equals(username)) {
                    return true;
                }
            }
        } catch (FileNotFoundException e) {
            return false;
        } catch (IOException e) {
            System.out.println("Erro ao verificar se o usuário existe: " + e.getMessage());
        }
        return false;
    }

    public static Usuario autenticarUsuario(String username, String senha) {
        try (BufferedReader br = new BufferedReader(new FileReader(CSV_FILE))) {
            String linha;
            while ((linha = br.readLine()) != null) {
                String[] data = linha.split(",");
                if (data.length >= 6 && data[4].equals(username) && data[5].equals(senha)) {
                    return new Usuario(data[0], Double.parseDouble(data[1]), data[2], Double.parseDouble(data[3]), data[4], data[5]);
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("Erro! O sistema não encontrou o arquivo de usuários.");
        } catch (IOException e) {
            System.out.println("Erro ao autenticar o usuário: " + e.getMessage());
        }
        return null;
    }

    public static String obterObjetivoTreino() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Você tem experiência em musculação? (sim/não): ");
        String experiencia = scanner.nextLine().trim().toLowerCase();

        if (experiencia.equals("sim")) {
            System.out.print("Há quanto tempo você treina? ");
            scanner.nextLine(); 
        }

        System.out.println("Escolha o objetivo do seu treino:");
        System.out.println("a) Ganhar massa muscular");
        System.out.println("b) Ganhar peso");
        System.out.println("c) Perder gordura");
        System.out.println("d) Perder peso");
        System.out.println("e) Melhorar condicionamento físico");
        System.out.println("f) Tonificar");

        return scanner.nextLine().trim().toLowerCase();
    }

    public static void gerarPlanoTreino(String objetivo) {
        System.out.println("\nSeu plano de treino personalizado:");

        switch (objetivo) {
            case "a":
                System.out.println("GANHAR MASSA MUSCULAR :");

                System.out.println("Segunda-feira (Peito e Tríceps):");
                System.out.println("- Supino reto: 4 séries de 8-10 repetições");
                System.out.println("- Crucifixo: 3 séries de 12 repetições");
                System.out.println("- Tríceps testa: 3 séries de 10 repetições");

                System.out.println("Terça-feira (Costas e Bíceps):");
                System.out.println("- Barra fixa: 4 séries de 6-8 repetições");
                System.out.println("- Remada curvada: 3 séries de 10 repetições");
                System.out.println("- Rosca direta: 3 séries de 12 repetições");

                System.out.println("Quarta-feira (Pernas):");
                System.out.println("- Agachamento: 4 séries de 8 repetições");
                System.out.println("- Leg press: 3 séries de 10 repetições");
                System.out.println("- Cadeira extensora: 3 séries de 12 repetições");

                System.out.println("Quinta-feira (Ombros e Trapézio):");
                System.out.println("- Desenvolvimento militar: 4 séries de 8 repetições");
                System.out.println("- Elevação lateral: 3 séries de 12 repetições");
                System.out.println("- Encolhimento de ombros: 3 séries de 10 repetições");

                System.out.println("Sexta-feira (Abdômen e Lombar):");
                System.out.println("- Prancha: 3 séries de 30-60 segundos");
                System.out.println("- Crunch: 3 séries de 15 repetições");
                System.out.println("- Hiperextensão lombar: 3 séries de 12 repetições");
                break;

            case "b":
                System.out.println("GANHAR PESO:");
                System.out.println("Segunda-feira (Peito e Tríceps):");
                System.out.println("- Supino reto: 4 séries de 8-10 repetições");
                System.out.println("- Crucifixo: 3 séries de 12 repetições");
                System.out.println("- Tríceps testa: 3 séries de 10 repetições");

                System.out.println("Terça-feira (Costas e Bíceps):");
                System.out.println("- Barra fixa: 4 séries de 6-8 repetições");
                System.out.println("- Remada curvada: 3 séries de 10 repetições");
                System.out.println("- Rosca direta: 3 séries de 12 repetições");

                System.out.println("Quarta-feira (Pernas):");
                System.out.println("- Agachamento: 4 séries de 8 repetições");
                System.out.println("- Leg press: 3 séries de 10 repetições");
                System.out.println("- Cadeira extensora: 3 séries de 12 repetições");

                System.out.println("Quinta-feira (Ombros e Trapézio):");
                System.out.println("- Desenvolvimento militar: 4 séries de 8 repetições");
                System.out.println("- Elevação lateral: 3 séries de 12 repetições");
                System.out.println("- Encolhimento de ombros: 3 séries de 10 repetições");

                System.out.println("Sexta-feira (Abdômen e Lombar):");
                System.out.println("- Prancha: 3 séries de 30-60 segundos");
                System.out.println("- Crunch: 3 séries de 15 repetições");
                System.out.println("- Hiperextensão lombar: 3 séries de 12 repetições");
                break;

            case "c":
                System.out.println("PERDER GORDURA:");
                System.out.println("Segunda a Sexta-feira (Treino HIIT):");
                System.out.println("- Corrida em alta intensidade (30 segundos)");
                System.out.println("- Descanso ativo (30 segundos) por 20 minutos");
                System.out.println("- Agachamento com salto: 3 séries de 12 repetições");
                System.out.println("- Burpees: 3 séries de 10 repetições");
                System.out.println("- Prancha lateral: 3 séries de 30 segundos de cada lado");
                System.out.println("- Mountain climbers: 3 séries de 20 repetições");
                break;

            case "d":
                System.out.println("PERDER PESO:");
                System.out.println("- Exercícios de resistência combinados com treinos aeróbicos de longa duração, como corrida leve ou caminhada rápida, por 45 minutos a 1 hora.");
                break;

            case "e":
                System.out.println("MELHORAR CONDICIONAMENTO FÍSICO:");
                System.out.println("Segunda a Sexta-feira (Cardio):");
                System.out.println("- Corrida, bicicleta ou elíptico por 30 minutos");
                System.out.println("- Kettlebell swing: 3 séries de 15 repetições");
                System.out.println("- Bosu ball squats: 3 séries de 12 repetições");
                System.out.println("- Jumping jacks: 3 séries de 20 repetições");
                break;

            case "f":
                System.out.println("TONIFICAR:");
                System.out.println("Segunda-feira (Peito e Tríceps):");
                System.out.println("- Supino inclinado: 4 séries de 12-15 repetições");
                System.out.println("- Tríceps no banco: 3 séries de 12 repetições");

                System.out.println("Terça-feira (Costas e Bíceps):");
                System.out.println("- Puxada alta: 4 séries de 12 repetições");
                System.out.println("- Rosca concentrada: 3 séries de 15 repetições");

                System.out.println("Quarta-feira (Pernas):");
                System.out.println("- Avanço: 3 séries de 15 repetições");
                System.out.println("- Stiff: 3 séries de 12 repetições");
                System.out.println("- Levantamento Terra Romeno: 4 séries de 8 repetições");
                System.out.println("- Agachamento Frontal com Barra: 3 séries de 10 repetições");
                break;

            default:
                System.out.println("Objetivo não reconhecido. Por favor, escolha uma opção válida.");
        }
    }

    public static void salvarUsuarioNoCsv(Usuario usuario) {
        boolean arquivoExiste = new File(CSV_FILE).exists();
        try (FileWriter writer = new FileWriter(CSV_FILE, true);
             PrintWriter printWriter = new PrintWriter(writer)) {

            if (!arquivoExiste) {
                printWriter.println("Nome,Altura,Sexo,Peso,Username,Senha,IMC,Status IMC");
            }

            String[] data = usuario.toCsvRow();
            printWriter.println(String.join(",", data));

        } catch (IOException e) {
            System.out.println("Erro ao salvar os dados no CSV: " + e.getMessage());
        }
    }

    public static void sugerirDieta(String objetivo) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("\nDeseja seguir uma dieta para potencializar seus resultados? (sim/não)");
        String resposta = scanner.nextLine().trim().toLowerCase();

        if (resposta.equals("sim")) {
            switch (objetivo) {
                case "a":
                    System.out.println("DIETA PARA GANHAR MASSA MUSCULAR:");
                    System.out.println("Café da manhã:");
                    System.out.println("- Omelete de claras de ovos com espinafre e tomate");
                    System.out.println("- Aveia com leite desnatado e frutas vermelhas");
                    System.out.println("Lanche da manhã:");
                    System.out.println("- Iogurte grego com amêndoas");
                    System.out.println("Almoço:");
                    System.out.println("- Peito de frango grelhado com quinoa e legumes no vapor");
                    System.out.println("Lanche da tarde:");
                    System.out.println("- Shake de proteína com banana e manteiga de amendoim");
                    System.out.println("Jantar:");
                    System.out.println("- Salmão assado com batata-doce e brócolis");
                    System.out.println("Ceia:");
                    System.out.println("- Queijo cottage com morangos");
                    break;

                case "b":
                    System.out.println("DIETA PARA GANHAR PESO:");
                    System.out.println("Café da manhã:");
                    System.out.println("- Vitamina de banana com aveia e leite integral");
                    System.out.println("Lanche da manhã:");
                    System.out.println("- Mix de castanhas e frutas secas");
                    System.out.println("Almoço:");
                    System.out.println("- Arroz integral com feijão, bife acebolado e salada");
                    System.out.println("Lanche da tarde:");
                    System.out.println("- Sanduíche de pasta de amendoim com banana");
                    System.out.println("Jantar:");
                    System.out.println("- Massa integral com molho de tomate e frango desfiado");
                    System.out.println("Ceia:");
                    System.out.println("- Iogurte com granola");
                    break;

                case "c":
                    System.out.println("DIETA PARA PERDER GORDURA:");
                    System.out.println("Café da manhã:");
                    System.out.println("- Smoothie de proteína com espinafre e abacate");
                    System.out.println("Lanche da manhã:");
                    System.out.println("- Cenouras baby com homus");
                    System.out.println("Almoço:");
                    System.out.println("- Salada de frango grelhado com folhas verdes e azeite de oliva");
                    System.out.println("Lanche da tarde:");
                    System.out.println("- Iogurte desnatado com chia");
                    System.out.println("Jantar:");
                    System.out.println("- Peixe assado com aspargos");
                    System.out.println("Ceia:");
                    System.out.println("- Chá de camomila");
                    break;

                case "d":
                    System.out.println("DIETA PARA PERDER PESO:");
                    System.out.println("Café da manhã:");
                    System.out.println("- Omelete de claras com cogumelos e espinafre");
                    System.out.println("Lanche da manhã:");
                    System.out.println("- Maçã com amêndoas");
                    System.out.println("Almoço:");
                    System.out.println("- Salada de atum com grão-de-bico e rúcula");
                    System.out.println("Lanche da tarde:");
                    System.out.println("- Iogurte light com morangos");
                    System.out.println("Jantar:");
                    System.out.println("- Frango grelhado com abobrinha e tomate");
                    System.out.println("Ceia:");
                    System.out.println("- Chá de hortelã");
                    break;

                case "e":
                    System.out.println("DIETA PARA MELHORAR CONDICIONAMENTO FÍSICO:");
                    System.out.println("Café da manhã:");
                    System.out.println("- Omelete de claras com espinafre e tomate");
                    System.out.println("- Pão integral com abacate");
                    System.out.println("Lanche da manhã:");
                    System.out.println("- Frutas frescas (como maçã ou pera)");
                    System.out.println("Almoço:");
                    System.out.println("- Peito de frango grelhado com arroz integral e brócolis");
                    System.out.println("Lanche da tarde:");
                    System.out.println("- Iogurte natural com granola");
                    System.out.println("Jantar:");
                    System.out.println("- Salmão assado com batata-doce e espargos");
                    System.out.println("Ceia:");
                    System.out.println("- Chá de hortelã");
                    break;

                case "f":
                    System.out.println("DIETA PARA TONIFICAR:");
                    System.out.println("Café da manhã:");
                    System.out.println("- Vitamina de banana com aveia e leite integral");
                    System.out.println("Lanche da manhã:");
                    System.out.println("- Sanduíche de pasta de amendoim com banana");
                    System.out.println("Almoço:");
                    System.out.println("- Arroz integral com feijão, bife acebolado e salada");
                    System.out.println("Lanche da tarde:");
                    System.out.println("- Iogurte desnatado com chia");
                    System.out.println("Jantar:");
                    System.out.println("- Massa integral com molho de tomate e frango desfiado, com legumes à vontade");
                    System.out.println("Ceia:");
                    System.out.println("- Iogurte com granola");
                    break;

                default:
                    System.out.println("Objetivo não reconhecido. Não foi possível gerar uma dieta.");
            }
            System.out.println("Dieta adicionada! Programa encerrado com sucesso!");
        } else {
            System.out.println("Programa encerrado com sucesso!");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Bem-vindo ao Healthy Life, o seu mais novo Sistema de Controle de Dieta e Treinamento Personalizado!");

        System.out.println("(1) - Quer se cadastrar?");
        System.out.println("(2) - Já possui um cadastro?");
        int escolha = scanner.nextInt();
        scanner.nextLine(); 

        Usuario usuario = null;

        if (escolha == 1) {
            usuario = recolherInformacoesUsuario();
            System.out.printf("\nIMC: %.2f - %s\n", usuario.calcularImc(), usuario.verificarStatusImc());
            salvarUsuarioNoCsv(usuario);
        } else if (escolha == 2) {
            System.out.print("Digite seu nome de usuário: ");
            String username = scanner.nextLine();
            System.out.print("Digite sua senha: ");
            String senha = scanner.nextLine();

            usuario = autenticarUsuario(username, senha);
            if (usuario == null) {
                System.out.println("Usuário ou senha incorretos. Tente novamente.");
                return;
            }
            System.out.printf("\nIMC: %.2f - %s\n", usuario.calcularImc(), usuario.verificarStatusImc());
        } else {
            System.out.println("Opção inválida.");
            return;
        }

        String objetivoTreino = obterObjetivoTreino();
        gerarPlanoTreino(objetivoTreino);
        sugerirDieta(objetivoTreino);
    }
}
