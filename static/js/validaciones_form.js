
$(document).on('showalert', '.alert', function(event,tiempo){
    window.setTimeout($.proxy(function() {
        $(this).fadeTo(500, 0).slideUp(500, function(){
            $(this).remove(); 
       	});
    }, this), tiempo);
}); 

/*
	FUNCION PARA VALIDAR QUE:
		- NO PONGAN LETRAS EN VES DE NUMEROS -> EJ: aa-bb-cc
		- LA FECHA SIGA EL FORMATO PARA QUE EL SERVIDOR NO ENTRE EN CONFLICTO
	PARAMETROS:
		fecha -> ARREGLO DE 3 POSICIONES 
			POSICION 0 -> DIA
					 1 -> MES
					 2 -> AÑO
*/
function validarFormato(fecha){
	if(fecha[0].length==2 && fecha[1].length==2 && fecha[2].length==4){ //valida que esten dos caracteres en cada posicion dia-mes-año
		if(!isNaN(fecha[0]) && !isNaN(fecha[1]) && !isNaN(fecha[2])){ // valida que dia, mes y año sean numeros y no cualquier otra cosa.		
			return true; // todo bien, el formato cumple.
		}
	}
	
	return false; //el formato no cumple
}


function validarFecha(desde,hasta){
			/*

			VALIDAR SI LA FECHA "DESDE" VA ANTES DE LA FECHA "HASTA"
			POSICION 0 PARA DIA, 1 PARA MES Y 2 PARA AÑO
			ENVIARA TRUE  SI LAS FECHAS NO SON VALIDAS 

			*/
			var msj="";
			var no_cumple=false;
			if(desde!=""){
				if(desde.length!=3 || !validarFormato(desde) ){ 
						msj+="<li><strong>Desde:</strong> Formato invalido <br></li>";
						no_cumple=true;
				}else{
						if(hasta!=""){
								if(hasta.length!=3 || !(validarFormato(hasta))){										
										msj+="<li><strong>Hasta:</strong> Formato invalido </li>";
										no_cumple=true;
								}else{
									var desde= new Date(desde[2],desde[1],desde[0]);
									var hasta= new Date(hasta[2],hasta[1],hasta[0]);
									if(desde>=hasta){
											msj+="<li><strong>Desde/Hasta:</strong> Rango de fechas invalidas </li>";
											no_cumple=true;
									}
								}
						}
				}

			}else{ 
				msj+="<li><strong>Desde:</strong> Campo obligatorio <br></li>";
				no_cumple=true;

			}
			if(no_cumple){
				create_alert(msj,"ERROR","aviso",false,0);
				return true;
			}else{
				return false;
			}
		}


function validarCombo(combo){
	//alert(combo.value);
	if(combo.value==""){
		return true; // NO HA SELECCIONADO NADA
	}
	else{
		return false;
	}
}



 function create_alert(mensaje, tipo_alerta, div_padre, emergente,tiempo){
    	/*
		RECIBE:
    		mensaje ---> LA CADENA CON EL MENSAJE A MOSTRAR.
    		tipo_alerta ---> EL TIPO DE ALERTA QUE SE DESEA EJECUTAR, IMPLICA LO SIGUIENTE:
    			EXITO ----------- "success" ----------- glyphicon glyphicon-ok-sign
				ERROR ----------- "danger" ------------ glyphicon glyphicon-remove-sign
				INFO ------------ "info" -------------- glyphicon glyphicon-info-sign
			div_padre ---> NOMBRE DEL DIV DONDE SE DESEA MOSTRAR EL MENSAJE
			emergente ---> TRUE SI VA A DESAPARECER EN UN DETERMINADO TIEMPO, DE LO CONTRARIO QUEDARA ESTATICO. 
			tiempo ---> EN EL CASO DE LAS EMERGENTES, EL TIEMPO QUE SE VA A TARDAR EN PANTALLA
    	*/

    var padre="#" + div_padre;
    var cad='';
    switch(tipo_alerta) {
    	case "EXITO":
    		var msj_aux='<b>¡Éxito!</b>';
    		var tipo= 'success';
    		var icono='check';
    		break;
    	case "ERROR":
    		var msj_aux= '<b>Atención.</b> <small style="color: black">Se han encontado los siguientes inconvenientes:</small>';
    		var tipo= 'danger';
    		var icono='exclamation';
    		break;
    	case "INFO":
    		var msj_aux='<b>Información</b>';
    		var tipo= 'info';
    		var icono='info';
    		break;
    	case "WAR":
    		var msj_aux='<b>Validación.</b> <small>Por favor verifique la siguiente información:</small>';
    		var tipo= 'warning';
    		var icono='exclamation-triangle';
    		break;
    }

    if(emergente){
	    cad+= '<div class="alert alert-'+ tipo+ '">\
	    		<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>';
	    cad+= '<strong style="font-size: 20px;"><i  class="fa fa-'+icono+ '"></i>  ' + msj_aux + '</strong><br/>';
	     cad+= '<div style="margin-left:5%;"><ul>' + mensaje + '</ul></div>';
	    $(cad).appendTo(padre).trigger('showalert',[tiempo]);
    }else{
    	cad+= '<div style="margin: 2%" class="alert alert-'+ tipo+ '"> <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a> \
    			';
	    cad+= '<strong style="font-size: 15px;"><i  class="fa fa-'+icono+ '"></i>  ' + msj_aux + '</strong><br/>';
	    cad+= '<div style="margin-left:5%;"><ul>' + mensaje + '</ul></div></div>';
    	document.getElementById(div_padre).innerHTML=cad;
    }
 }


/*
	FUNCIÓN QUE PERMITE GENERAR UN ALERT DE TIPO INFORMACIÓN PARA FORMULARIOS
	RECIBE:
		tipo_accion ---> STRING DE QUE TIPO DE ACCIÓN SE PLANEABA REALIZAR.
		div_padre ---> NOMBRE DEL DIV DONDE SE MOSTRARÁ LA ALERTA
		emergente ---> TRUE SI VA A DESAPARECER EN UN DETERMINADO TIEMPO, DE LO CONTRARIO QUEDARA ESTATICO. 
		tiempo ---> EN EL CASO DE LAS EMERGENTES, EL TIEMPO QUE SE VA A TARDAR EN PANTALLA
*/

function info_seleccion(tipo_accion,div_padre,emergente,tiempo){
	var cad= "Debe seleccionar un registro para realizar la " + tipo_accion;
	create_alert(cad,"INFO",div_padre,emergente,tiempo);
}

/*
	FUNCIÓN QUE PERMITE GENERAR UN ALERT DE TIPO WARNING PARA FORMULARIOS
	UTILIZAR EN VALIDACIONES CUYOS MENSAJES PROVIENEN DEL SERVIDOR.
	RECIBE:
		json ---> VARIABLE DE TIPO JSON QUE CONTIENE LA LLAVE "ERRORS" QUE ES UN DICCIONARIO QUE SE IMPRIMIRÁ EN PANTALLA.
		div_padre ---> NOMBRE DEL CONTENEDOR EN DONDE SE COLOCARÁ EL CÓDIGO DEL ALERT.

*/
function show_errors(json, div_padre){
	var json_keys= Object.keys(json["errors"]);
	var message='';
	for (var i = json_keys.length - 1; i >= 0; i--) {
		message+="<li> <strong class='text-capitalize'>" + correc_palabras(json_keys[i].toString())  + ": </strong>" + json['errors'][json_keys[i]][0] + "</li>";
	};
	create_alert(message,"ERROR",div_padre,false,0);
}

function correc_palabras(palabra){
	/*
		Corrección de ortográfia para el form.errors de Django.
	*/
	console.log(palabra);
	var arr_palabras=[
				['telefono','Teléfono'],
				['correo_contacto','Correo Electrónico del contacto'],
				['telefono_contacto','Teléfono de contacto'],
				['registro_iva','Registro de IVA'],
				['horas_posibles','Horas posibles'],
				['hora_apertura','Hora de apertura'],
				['hora_cierre','Hora de cierre']
				//['']
				];
	
	for(var i=0;i<arr_palabras.length;i++){
		if(palabra==arr_palabras[i][0]){

			palabra=arr_palabras[i][1];
		}
	}
	return palabra.capitalize();
}

String.prototype.capitalize = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
}

	
function datatable_catchError(){
	/*bootbox.alert(
		"<br><div class='alert alert-danger'> </div>");*/
	mensaje="<br><div class='alert alert-danger'>"
	mensaje+="<strong>Atención</strong> <i class='ace-icon fa fa-wrench icon-animated-wrench bigger-125'></i><br>"
	mensaje+="Ocurrío un inconveniente. Por favor intentelo más tarde." 
	mensaje+="</div>"
	bootbox.dialog({
	  message: mensaje
	});
}
