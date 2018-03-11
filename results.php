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
        <div>
          <h4>Resultados del metodo de Validacion Cruzada con _ pliegues</h4>
        </div>


      <table>
        <thead>
          <tr>
            <th colspan="5">Matriz de Confusión</th>
          </tr>
        </thead>

        <tbody>

          <?php
            $data = file_get_contents("confusionfinal.txt"); //read the file
            $convert = explode("\n", $data); //create array separate by new line

            $fila1= explode("\t", $convert[0]);
            $fila2= explode("\t", $convert[1]);
            $fila3= explode("\t", $convert[2]);
            $fila4= explode("\t", $convert[3]);
            $fila5= explode("\t", $convert[4]);
          ?>


          <tr>
            <td><?php echo $fila1[0]; ?></td>
            <td><?php echo $fila1[1]; ?></td>
            <td><?php echo $fila1[2]; ?></td>
            <td><?php echo $fila1[3]; ?></td>
            <td><?php echo $fila1[4]; ?></td>
          </tr>
          <tr>
            <td><?php echo $fila2[0]; ?></td>
            <td><?php echo $fila2[1]; ?></td>
            <td><?php echo $fila2[2]; ?></td>
            <td><?php echo $fila2[3]; ?></td>
            <td><?php echo $fila2[4]; ?></td>
          </tr>
          <tr>
            <td><?php echo $fila3[0]; ?></td>
            <td><?php echo $fila3[1]; ?></td>
            <td><?php echo $fila3[2]; ?></td>
            <td><?php echo $fila3[3]; ?></td>
            <td><?php echo $fila3[4]; ?></td>
          </tr>
          <tr>
            <td><?php echo $fila4[0]; ?></td>
            <td><?php echo $fila4[1]; ?></td>
            <td><?php echo $fila4[2]; ?></td>
            <td><?php echo $fila4[3]; ?></td>
            <td><?php echo $fila4[4]; ?></td>
          </tr>
          <tr>
            <td><?php echo $fila5[0]; ?></td>
            <td><?php echo $fila5[1]; ?></td>
            <td><?php echo $fila5[2]; ?></td>
            <td><?php echo $fila5[3]; ?></td>
            <td><?php echo $fila5[4]; ?></td>
          </tr>


        </tbody>
      </table>


   </body>
</html>
