package br.ufal.aracomp.cosmos.conectorsimples;

import br.ufal.aracomp.cosmos.emprestimo.spec.req.ILimiteReq;
import br.ufal.aracomp.cosmos.limite.spec.prov.ILimiteOps;

public class ConectorSimples implements ILimiteOps {
	ILimiteOps limiteOps;
	
	public ConectorSimples(ILimiteOps limiteOps) {
		this.limiteOps = limiteOps;
	}
	
	@override 
	public double estimarLimite(DTUsuario usuario) {
		DTCliente cliente = new DTCliente ();
		cliente.salario = Double.parseDouble(usuario.rendimentos);
		return this.limiteOps.calcularLimite(cliente);
	}

}
