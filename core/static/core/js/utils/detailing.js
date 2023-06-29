const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const telefonoRegex = /^(\+?56)?(\s?)(0?9)(\s?)[98765432]\d{7}$/;
const rutRegex = /^0*(\d{1,3}(\.?\d{3})*)\-?([\dkK])$/;
const dvEsperadoMap = {
    10: "K",
    11: 0
};

function dgv(rut)    //digito verificador
{  
      let M = 0;
      let S = 1;

	  for(; rut ;rut = Math.floor(rut / 10)) {
        S = ( S + rut % 10 * ( 9 - M++ % 6) ) % 11;
      }
	  //return S?S-1:'k';
      
      return (S ? S - 1 : 'k');
 }

export const validaEmail = email => {
    return emailRegex.test(email);
};

/* JS function that'll validate a chilean rut */
export const validaRut = rut => {
    rut = rut.replace(/[.-]/g, '');
  
    if (!rutRegex.test(rut)) {
        return false;
    }
    const rutSinDigito = rut.slice(0, -1);
    const rutSinDigitoArr = rutSinDigito.split("");
    const digitoVerificador = rut.slice(-1).toUpperCase();
    const rutSinDigitoArrInverso = rutSinDigitoArr.reverse();
    
    const suma = rutSinDigitoArrInverso.reduce((acumulador, actual, i) => {

        const multiplo = (i % 6) + 2;

        return acumulador + actual * multiplo;
      }, 0);

    let dvEsperado = 11 - (suma % 11);

    dvEsperado = dvEsperadoMap[dvEsperado] || dvEsperado;

    return digitoVerificador === dvEsperado;
}

export const validaTelefono = telefono => {
    return telefonoRegex.test(telefono);
}