// const btnDelete = document.querySelectorAll('.btn-delete') /* busca todos las clases que contengan (btn-delete) y guardo en una constante, devolviendome una lista de arreglos*/
// /*proximo codigo es puro javasCript*/
// if (btnDelete) {
// /*si contiene algun boton con esta clase (existe)... lo transformo en un arreglo*/
//    const btnArray = Array.from(btnDelete); /*guardo esse array en una constante */
//    btnArray.forEach((btn) => { /* y lo recorro, diciendo: "por cada boton que voy recorriendo (btn)"  */
//     btn.addEventListener('click', (e) =>{ /* agrego un evento de escucha (click), toma la info del evento (e) */
//         if(!confirm('Estas seguro que quieres eliminar...?')){ /* si aparece una ventana de CONFIRM, aparecera el string deseado */
//             e.preventDefault(); /* si confirma el evento, !confirm se transforma el false, y el if mostrara el evento, de lo contrario el if quedara igual (e.preventDefault) */
//         }
//     });
//    });
// } 

const btnDelete = document.querySelectorAll('.btn-delete') /* busca todos las clases que contengan (btn-delete) y guardo en una constante, devolviendome una lista de arreglos*/
/*proximo codigo es puro javasCript*/
if (btnDelete) {
/*si contiene algun boton con esta clase (existe)... lo transformo en un arreglo*/
   const btnArray = Array.from(btnDelete); /*guardo esse array en una constante */
   btnArray.forEach((btn) => { /* y lo recorro, diciendo: "por cada boton que voy recorriendo (btn)"  */
    btn.addEventListener('click', (e) =>{ /* agrego un evento de escucha (click), toma la info del evento (e) */
        if(confirm('Estas seguro que quieres eliminar...?')){ 
            /*AQUI NO ES PRECISO ADICIONAR NADA */
        } else{
            e.preventDefault()
        }
    });
   });
} 

/*  EN ESTE ULTIMO EL CODIGO SOLO MODIFICA LA NEGACION DEL (CONFIRM), ES OTRA VARIABLE DE CODIGO CON EL MIMSO FIN */