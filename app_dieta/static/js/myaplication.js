
function funcao_valor_total___() {
    var num1 = document.querySelector(".valorItem").value;
    var num2 = document.querySelector(".quantidadeItens").value;
    //var num1 = 2.98;

    //var num3 = document.getElementById(num1).value.replace('.', ',');
    //var num1 = parseFloat(num3) *100;


    //document.write(num1);
    //document.write(Number.parseFloat(num1));

    var vl_total_itens = num1 * num2;

    //document.write(Number.isNaN(vl_total_itens));
        //-- COM R$
    //var vl_total_itens = vl_total_itens.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });

        //-- SEM R$
    var vl_total_itens = vl_total_itens.toLocaleString('pt-br', {minimumFractionDigits: 2});

    //document.querySelector(".resultado").innerHTML = vl_total_itens;

    campoTotal.value = vl_total_itens;
    campoTotal2.value = vl_total_itens;

}

function funcao_valor_total() {
    var varTotal = (document.getElementById("campoValorUnitario").value *
                    document.getElementById("campoQuantidade").value)

    document.getElementById("campoTotal",id).value = varTotal

    document.getElementById("campoTotal2").value =
               document.getElementById("campoTotal").value

}

function validaEmail() {
    if (!document.CadUsuarioForm.email.value.includes("@")){
        alert("E-mail invalido!");

    }
}

function avisoFazerLogin() {
     alert("Para comprar, Faça o LOGIN ou cadastre-se!");
}

function avisoSemItemNoCarrinho() {
    alert("Atenção! Nao há item no carrinho!");

}

function avisoSemEnderecoEntrega(){
    alert("Atenção! Cadastre um endereço de entrega!");
}


function botaoMaisUm(id,vlUnitario){

    var _varTotal =0;
    var totalDelivery =0;
    var maisUm = document.getElementById("campoQuantidade"+id).value
    var maisUm =  parseFloat(maisUm) + 1
    document.getElementById("campoQuantidade"+id).value = maisUm
   
    _varTotal = (vlUnitario *
                     document.getElementById("campoQuantidade"+id).value)

    //var _varTotal = document.getElementById("campoValorUnitario").value
    //alert(_varTotal)
   
    totalDelivery = (parseFloat(document.getElementById("valorTotalDelivery").value) + vlUnitario)

    document.getElementById("campoTotal"+id).value = _varTotal;
    document.getElementById("valorTotalDelivery").value =  totalDelivery;


    alteraVirgula(id)


    /**
    if (maisUm > 0){
        document.getElementById("corDeFundoPreco"+id).
                style.backgroundColor= "#90EE90";
        document.getElementById("cor-de-fundo-imagem"+id).
                style.backgroundColor= "#90EE90";

    }
    **/

}

function botaoMenosUm(id,vlUnitario){

    var _varTotal =0;
    var totalDelivery =0;
    var menosUm = document.getElementById("campoQuantidade"+id).value;
    var menosUm =  menosUm - 1;
    document.getElementById("campoQuantidade"+id).value = menosUm;

    if (menosUm <0) {
        var menosUm =0;
        document.getElementById("campoQuantidade"+id).value = menosUm; 
        vlUnitario =0; 
        alert("Quantidade não pode ser menos que 0 (ZERO)!");
    }

    var varTotal = (vlUnitario *
                    document.getElementById("campoQuantidade"+id).value);

   
    totalDelivery = 
            (parseFloat(document.getElementById("valorTotalDelivery").value) - vlUnitario)

    document.getElementById("campoTotal"+id).value = varTotal
    document.getElementById("valorTotalDelivery").value =  totalDelivery;
    alteraVirgula(id);
    
  
    /**
    if (menosUm < 1){
        document.getElementById("corDeFundoPreco"+id).
                style.backgroundColor= "white";
        document.getElementById("cor-de-fundo-imagem"+id).
                style.backgroundColor= "white"; 
    }
    **/
    
}

function alteraVirgula(id){
    document.getElementById("valor_unitario"+id).value = 
            document.getElementById("valor_unitario"+id).value.replace(",", ".")

    document.getElementById("campoTotal"+id).value = 
            document.getElementById("campoTotal"+id).value.replace(",", ".")
    
}









