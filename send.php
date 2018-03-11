<html>
   <head>
      <title>The Materialize Form Example</title>
      <meta name = "viewport" content = "width = device-width, initial-scale = 1">
      <link rel = "stylesheet"
         href = "https://fonts.googleapis.com/icon?family=Material+Icons">
      <link rel = "stylesheet"
         href = "https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.3/css/materialize.min.css">
      <script type = "text/javascript"
         src = "https://code.jquery.com/jquery-2.1.1.min.js"></script>
      <script src = "https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.3/js/materialize.min.js">
      </script>
   </head>

   <body class = "container">
        <nav>
          <div class="nav-wrapper">
            <a href="#" class="brand-logo center">Mineria de Datos</a>

          </div>
        </nav>
        <nav>
          <div class="nav-wrapper">
            <ul id="nav-mobile" class="left hide-on-med-and-down">
              <li><a href="index.php">Inicio</a></li>
              <li><a href="send.php">Guardar Registros</a></li>
              <li><a href="list.php">Listar Registros</a></li>
              <li><a href= "cross.php">Validacion cruzada</a><li>
            </ul>
          </div>
        </nav>
        <br>
        <hr>
        <br>

      <div class = "row">
         <form class = "col s12" action="save.php" method="POST">
            <div class = "row">

               <div class = "input-field col s6">
               <i class = "material-icons prefix">account_circle</i>
                  <input placeholder = "e.g.23"  id = "edad" name = "edad"
                     type = "number" class = "active validate" min ="0" max="100" required />
                  <label for = "name">Edad</label>
               </div>

               <div class = "input-field col s6">
               <i class = "material-icons prefix">account_circle</i>
                  <label for = "password">Nivel de sodio</label>
                  <input id = "sodio" name ="sodio" placeholder="e.g.0,0008" type = "number" min ="0" max="1" step="0.0001"
                     class = "validate" required />
               </div>
            </div>

            <div class = "row">
               <div class = "input-field col s6">
                  <i class = "material-icons prefix">account_circle</i>
                  <input  id = "potasio" name="potasio"
                     type = "number" placeholder="e.g.0,009" step="0.0001" class = "active validate" required />
                  <label for = "name">Nivel de Potasio</label>
               </div>

               <div class = "input-field col s6">
               <i class = "material-icons prefix">account_circle</i>
                  <label for = "password">Genero</label>
                  <input id = "genero" name="genero" type = "text" placeholder = "M or F"
                     class = "validate" required />
               </div>
            </div>

             <div class = "row">
               <div class = "input-field col s6">

                  <i class = "material-icons prefix">account_circle</i>
                  <input   id = "sanguinea" name="sanguinea"
                     type = "text" class = "active validate" placeholder="LOW or NORMAL or HIGH" required />
                  <label for = "name">Presion Sanguinea</label>
               </div>

               <div class = "input-field col s6">
               <i class = "material-icons prefix">account_circle</i>
                  <label for = "password">Colesterol</label>
                  <input id = "colesterol" type = "text"   placeholder='LOW or NORMAL or HIGH' name="colesterol"
                     class = "validate" required />
               </div>
            </div>

            <div class="row">

            <button class="btn waves-effect waves-light" type="submit" name="action">Enviar Registro
                 <i class="material-icons right">send</i>
            </button>
            </div>


         </form>
      </div>
   </body>
</html>
