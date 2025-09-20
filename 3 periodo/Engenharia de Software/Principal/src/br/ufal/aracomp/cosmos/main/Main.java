package br.ufal.aracomp.cosmos.main;

import br.ufal.aracomp.cosmos.emprestimo.impl.ComponentFactory;
import br.ufal.aracomp.cosmos.emprestimo.impl.IManager;
import br.ufal.aracomp.cosmos.emprestimo.spec.prov.IEmprestimoOps;
import br.ufal.aracomp.cosmos.limite.spec.dt.DTCliente;

public class Main {
	 public static void main(String[] args) {
		 
		IManager compEmp = ComponentFactory.creatInstance();
		IEmprestimoOps objEmpOps = (IEmprestimoOps)compEmp.getProvidedInterface("IEmprestimoOps");
		DTUsuario usuario = new DTUsuario();
		usuario.rendimentos = "1500";
		System.out.println(objEmpOs.liberarEmprestimoAutomatico(usuario));

	 }

}


