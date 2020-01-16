import time

text="""
<tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-11-1488-3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Ovulito fecundado. La historia del sapo Fog</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Muñoz Pedrals, Ricardo (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Universitaria S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1999-05-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-11-1489-0</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>El zorro Chilla</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Muñoz Pedrals, Ricardo (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Universitaria S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1999-05-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-0622-9</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Erase una vez... Un hermoso planeta llamado tierra</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1991-12-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-0630-4</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Erase una vez... Un hermoso planeta llamado tierra</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1992-03-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>2</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Inglés</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-0668-7</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos del tio Juan, el zorro Culpeo</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1992-05-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>4</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Inglés</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-0680-9</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos del tio Juan, el zorro Culpeo</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1992-07-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Inglés</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-0743-1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos para sonreir</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1992-10-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-0785-1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos de los derechos del niño</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1993-06-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Francés</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-0869-8</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos de los derechos del niño</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1994-04-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>2</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Alemán</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1129-2</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Los señores del átomo/El átomo</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl<br>Ramos Marías, Mariano (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1995-10-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1130-8</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Coseraut/Avance tecnológico</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl<br>Ramos Marías, Mariano (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1995-10-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1131-5</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Mis padres son un huevo/Célula y reproducción</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl<br>Ramos Marías, Mariano (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1995-10-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1132-2</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Madre nostrum/Los seres vivos y su medio</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl<br>Ramos Marías, Mariano (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1995-09-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1134-6</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Los hombres que hacían llover/Medio ambiente</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl<br>Ramos Marías, Mariano (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1995-10-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1135-3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Unos robots muy especiales/El cuerpo humano</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl<br>Ramos Marías, Mariano (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1995-10-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr>  <tr>
    <td colspan="3">
      <table width="100%" class="titletable">
        <tr>
					<td><a href="buscador.php">Nueva b&uacute;squeda</a></td>
          <td>128 resultados encontrados.</td>
					<td align="center">P&aacute;gina 1 / 9</td>
					<td align="right"><table><tr><td>&lt;&lt;</td><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=2">&gt;&gt;</a></td></tr></table></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
</div>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" >
<title>Agencia ISBN :: Cámara Chilena del libro</title>
<script type="text/javascript" src="./script.js?nocache=116108791"></script>
<link href="./ISBN_CSS.css" rel="stylesheet" type="text/css" >
<LINK REL="SHORTCUT ICON" HREF="./Imagenes/favicon.ico">

<style type="text/css">
<!--
select{
	border:#444444;
	border-style:solid;
	border-width:1px;
	font-family:Verdana, Arial, Helvetica, sans-serif;
	font-size:10px;
	color:#444444;
/*	display:block;	*/
}

#layerLogo {
	position:relative;
	left:65px;/*65*/
/*	top:61px;*/
	top:44px;
	width:250px;
	height:80px;
	z-index:4;
	background-image: url(./imagen.php?table=agencyparameter&field=logo&id=1);
}

#layerAdmin {
	position:relative;
	left:55px;
	top:474px;
	width:179px;
	height:133px;
	z-index:5;
}
#layerMenuTop {
	position:relative;
	left:62px;
	top:14px;
	width:866px;
	height:21px;
	z-index:6;
}
#layerMenuMiddle {
	position:relative;
	left:27px;
	top:147px;
	width:930px;
	height:10px;
	z-index:7;
}
#layerContForm {
	position:relative;
/*	width:100%;	*/
/*	height:100%;	*/
}
#layerCont {
	position:relative;
	left:20px;
	top:14px;
	width:946px;
	height:800px;
}
#footer {
	position:relative;
	left:280px;
	top:820px;
	width:482px;
	height:24px;
	z-index:8;
}
#menuAdmon {
	position:relative;
	left:175px;
	top:362px;
	width:580px;
	height:112px;
	z-index:10;
}
#LayerAgencia {
	position:relative;
	left:729px;
	top:76px;
	width:188px;
	height:52px;
	z-index:10;
	background-image: url(./Imagenes/IconBlackSmall.jpg);
}

-->
</style>
<style type="text/css">
.labelLogin {
	font:bold 11px Verdana, Arial, Helvetica, sans-serif;
}
#bannerHead {
	position:absolute;
	left:244px;
	top:20px;
	width:714px;
	height:125px;
	z-index:1;
	background-image: url(Imagenes/cabezote_isbn.jpg);
}

#menu {
/*width: 12em;*/
width: 100%;
}

#menu ul {
	list-style: none;
margin: 0;
padding: 0;
}

#menu a {
font: bold 11px/16px arial, helvetica, sans-serif;
display: block;
				 border-width: 1px;
				 border-style: solid;
				 border-color: #ccc #888 #555 #bbb;
margin: 0;
padding: 2px 3px;
}

#menu a {
	/*color: #000;*/
color: #fff;
			 /*background: #efefef;*/
background: #00246a;
						text-decoration: none;
}

#menu a:hover {
	/*color: #a00;
background: #fff;*/
background: #135AB0;
}

#menu li {
position: relative;
}

#menu ul ul ul {
position: absolute;
top: 0;
left: 100%;
width: 100%;
}

div#menu ul ul ul,
	div#menu ul ul li:hover ul ul
{display: none;}

div#menu ul ul li:hover ul,
	div#menu ul ul ul li:hover ul
{display: block;}

</style><!--[if IE]>

<style type="text/css" media="screen">

 #menu ul li {float: left; width: 100%;}

</style>

<![endif]--><!--[if lt IE 7]>

<style type="text/css" media="screen">

body {

behavior: url(csshover.htc);

					font-size: 100%;

} 

#menu ul li {float: left; width: 100%;}

#menu ul li a {height: 1%;} 



#menu a {

font: bold 9px arial, helvetica, sans-serif;

} 



</style>

<![endif]-->

<script type="text/javascript">
function show(_d)
{
  var _x = document.getElementById(_d);
 _x.style.visibility="visible";
}

function noShow(_d)
{
  var _x = document.getElementById(_d);
 _x.style.visibility="hidden";
}
-->
</script>
</head>
<body bgcolor="#FFFFFF">
<table align="center" width="930" border="0" cellpadding="0" cellspacing="0" style="height:100%">
	<tr>
		<td colspan="2">
			<table width="100%" cellpadding="0" cellspacing="0">
				<tr>
					<td height="125" valign="middle"><a href="http://www.camaradellibro.cl / www.isbnchile.cl"><img border="0" src="./imagen.php?table=agencyparameter&amp;field=logo&amp;id=1"></a></td>
					<td align="right">
											<img src="./Imagenes/IconBlackSmall.jpg">
										</td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td colspan="2">
			<table width="100%" cellpadding="0" cellspacing="0">
				<tr class="menuMiddle">
					<td bgcolor="#444444" width="20"></td>	
					<td bgcolor="#444444" height="20">
						Est&aacute; ubicado en: <a href="./login.php">Home</a>&nbsp;&rsaquo;&rsaquo;
						<a href="buscador.php">B&uacute;squeda de t&iacute;tulos</a>&nbsp;&rsaquo;&rsaquo; Resultados de la b&uacute;squeda					</td>
					<td bgcolor="#444444" onClick="closeSesion();" style="cursor:pointer;" align="right" width="112"><img src="./Imagenes/btnSesion.gif" width="112" height="19" align="middle"></td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td width="210" style="border: 1px solid #CCCCCC;" valign="top" align="center">
<div id="layerMenu">
	<table width="200">
		<tr><td align="center"><br><br><img src="Imagenes/searchLeft.jpg" width="77" height="428"></td></tr>
	</table>
</div>

		</td>
		<td style="border: 1px solid #CCCCCC;" valign="top">
<div id="layerContForm">
<br><br>
<table  width="500" border="0" align="center" cellpadding="0" cellspacing="2">
<tr><td colspan="3"><table width="100%" cellpadding="0" cellspacing="0" class="head_table"><tr><td bgcolor="#007520" NOWRAP>&nbsp;&rsaquo;&rsaquo;&nbsp;Resultados de la b&uacute;squeda&nbsp;&nbsp;</td><td width="17"><img src="Imagenes/imagen.php?icono=triangulo.png&amp;color=0,117,32"></td><td width="99%"><table width="100%" cellpadding="0" cellspacing="0"><tr><td height="16"></td></tr><tr><td height="3" style="background-image:url(Imagenes/imagen.php?icono=pixel.png&amp;color=0,117,32);"></td></tr></table></td></tr></table></td></tr>  <tr>
    <td colspan="3">
      <table width="100%" class="titletable">
        <tr>
					<td><a href="buscador.php">Nueva b&uacute;squeda</a></td>
          <td>128 resultados encontrados.</td>
					<td align="center">P&aacute;gina 2 / 9</td>
					<td align="right"><table><tr><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=1">&lt;&lt;</a></td><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=3">&gt;&gt;</a></td></tr></table></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1227-5</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos para adolescentes románticos</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1997-06-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Inglés</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1234-3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos para sonreir</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1997-08-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>2</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1253-4</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos para adolescentes románticos</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1998-05-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>5</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1257-2</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos del tío Juan, el zorro culpeo. (Delfín de color)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1998-06-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Inglés</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1258-9</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos del tío Juan, el zorro culpeo. (Obras escogidas)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1998-06-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>4</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1259-6</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Erase una vez un hermoso planeta llamado tierra</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1998-06-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>6</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1273-2</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos de los derechos del niño</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1998-08-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>5</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1290-9</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Erase una vez un hermoso planeta llamado tierra</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1999-03-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>8</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1323-4</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Erase una vez un hermoso planeta llamado tierra</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1999-07-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>8</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1365-4</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos para adolescentes románticos</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Oyarzún Robles, Pablo César  (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2000-05-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>8</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1373-9</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos transversales</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Concha Cosani, Silvana Beatriz (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2000-08-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1381-4</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos para sonreir (Delfín de color)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2000-09-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>2</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1382-1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos para sonreir (Obras escogidas)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2000-09-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1392-0</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos para adolescentes románticos (Obras escogidas)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2000-10-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>8</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1409-5</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos transversales</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Montt Moscoso, Alberto José (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2001-05-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr>  <tr>
    <td colspan="3">
      <table width="100%" class="titletable">
        <tr>
					<td><a href="buscador.php">Nueva b&uacute;squeda</a></td>
          <td>128 resultados encontrados.</td>
					<td align="center">P&aacute;gina 2 / 9</td>
					<td align="right"><table><tr><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=1">&lt;&lt;</a></td><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=3">&gt;&gt;</a></td></tr></table></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
</div>


<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" >
<title>Agencia ISBN :: Cámara Chilena del libro</title>
<script type="text/javascript" src="./script.js?nocache=1028192744"></script>
<link href="./ISBN_CSS.css" rel="stylesheet" type="text/css" >
<LINK REL="SHORTCUT ICON" HREF="./Imagenes/favicon.ico">

<style type="text/css">
<!--
select{
	border:#444444;
	border-style:solid;
	border-width:1px;
	font-family:Verdana, Arial, Helvetica, sans-serif;
	font-size:10px;
	color:#444444;
/*	display:block;	*/
}

#layerLogo {
	position:relative;
	left:65px;/*65*/
/*	top:61px;*/
	top:44px;
	width:250px;
	height:80px;
	z-index:4;
	background-image: url(./imagen.php?table=agencyparameter&field=logo&id=1);
}

#layerAdmin {
	position:relative;
	left:55px;
	top:474px;
	width:179px;
	height:133px;
	z-index:5;
}
#layerMenuTop {
	position:relative;
	left:62px;
	top:14px;
	width:866px;
	height:21px;
	z-index:6;
}
#layerMenuMiddle {
	position:relative;
	left:27px;
	top:147px;
	width:930px;
	height:10px;
	z-index:7;
}
#layerContForm {
	position:relative;
/*	width:100%;	*/
/*	height:100%;	*/
}
#layerCont {
	position:relative;
	left:20px;
	top:14px;
	width:946px;
	height:800px;
}
#footer {
	position:relative;
	left:280px;
	top:820px;
	width:482px;
	height:24px;
	z-index:8;
}
#menuAdmon {
	position:relative;
	left:175px;
	top:362px;
	width:580px;
	height:112px;
	z-index:10;
}
#LayerAgencia {
	position:relative;
	left:729px;
	top:76px;
	width:188px;
	height:52px;
	z-index:10;
	background-image: url(./Imagenes/IconBlackSmall.jpg);
}

-->
</style>
<style type="text/css">
.labelLogin {
	font:bold 11px Verdana, Arial, Helvetica, sans-serif;
}
#bannerHead {
	position:absolute;
	left:244px;
	top:20px;
	width:714px;
	height:125px;
	z-index:1;
	background-image: url(Imagenes/cabezote_isbn.jpg);
}

#menu {
/*width: 12em;*/
width: 100%;
}

#menu ul {
	list-style: none;
margin: 0;
padding: 0;
}

#menu a {
font: bold 11px/16px arial, helvetica, sans-serif;
display: block;
				 border-width: 1px;
				 border-style: solid;
				 border-color: #ccc #888 #555 #bbb;
margin: 0;
padding: 2px 3px;
}

#menu a {
	/*color: #000;*/
color: #fff;
			 /*background: #efefef;*/
background: #00246a;
						text-decoration: none;
}

#menu a:hover {
	/*color: #a00;
background: #fff;*/
background: #135AB0;
}

#menu li {
position: relative;
}

#menu ul ul ul {
position: absolute;
top: 0;
left: 100%;
width: 100%;
}

div#menu ul ul ul,
	div#menu ul ul li:hover ul ul
{display: none;}

div#menu ul ul li:hover ul,
	div#menu ul ul ul li:hover ul
{display: block;}

</style><!--[if IE]>

<style type="text/css" media="screen">

 #menu ul li {float: left; width: 100%;}

</style>

<![endif]--><!--[if lt IE 7]>

<style type="text/css" media="screen">

body {

behavior: url(csshover.htc);

					font-size: 100%;

} 

#menu ul li {float: left; width: 100%;}

#menu ul li a {height: 1%;} 



#menu a {

font: bold 9px arial, helvetica, sans-serif;

} 



</style>

<![endif]-->

<script type="text/javascript">
function show(_d)
{
  var _x = document.getElementById(_d);
 _x.style.visibility="visible";
}

function noShow(_d)
{
  var _x = document.getElementById(_d);
 _x.style.visibility="hidden";
}
-->
</script>
</head>
<body bgcolor="#FFFFFF">
<table align="center" width="930" border="0" cellpadding="0" cellspacing="0" style="height:100%">
	<tr>
		<td colspan="2">
			<table width="100%" cellpadding="0" cellspacing="0">
				<tr>
					<td height="125" valign="middle"><a href="http://www.camaradellibro.cl / www.isbnchile.cl"><img border="0" src="./imagen.php?table=agencyparameter&amp;field=logo&amp;id=1"></a></td>
					<td align="right">
											<img src="./Imagenes/IconBlackSmall.jpg">
										</td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td colspan="2">
			<table width="100%" cellpadding="0" cellspacing="0">
				<tr class="menuMiddle">
					<td bgcolor="#444444" width="20"></td>	
					<td bgcolor="#444444" height="20">
						Est&aacute; ubicado en: <a href="./login.php">Home</a>&nbsp;&rsaquo;&rsaquo;
						<a href="buscador.php">B&uacute;squeda de t&iacute;tulos</a>&nbsp;&rsaquo;&rsaquo; Resultados de la b&uacute;squeda					</td>
					<td bgcolor="#444444" onClick="closeSesion();" style="cursor:pointer;" align="right" width="112"><img src="./Imagenes/btnSesion.gif" width="112" height="19" align="middle"></td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td width="210" style="border: 1px solid #CCCCCC;" valign="top" align="center">
<div id="layerMenu">
	<table width="200">
		<tr><td align="center"><br><br><img src="Imagenes/searchLeft.jpg" width="77" height="428"></td></tr>
	</table>
</div>

		</td>
		<td style="border: 1px solid #CCCCCC;" valign="top">
<div id="layerContForm">
<br><br>
<table  width="500" border="0" align="center" cellpadding="0" cellspacing="2">
<tr><td colspan="3"><table width="100%" cellpadding="0" cellspacing="0" class="head_table"><tr><td bgcolor="#007520" NOWRAP>&nbsp;&rsaquo;&rsaquo;&nbsp;Resultados de la b&uacute;squeda&nbsp;&nbsp;</td><td width="17"><img src="Imagenes/imagen.php?icono=triangulo.png&amp;color=0,117,32"></td><td width="99%"><table width="100%" cellpadding="0" cellspacing="0"><tr><td height="16"></td></tr><tr><td height="3" style="background-image:url(Imagenes/imagen.php?icono=pixel.png&amp;color=0,117,32);"></td></tr></table></td></tr></table></td></tr>  <tr>
    <td colspan="3">
      <table width="100%" class="titletable">
        <tr>
					<td><a href="buscador.php">Nueva b&uacute;squeda</a></td>
          <td>128 resultados encontrados.</td>
					<td align="center">P&aacute;gina 3 / 9</td>
					<td align="right"><table><tr><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=2">&lt;&lt;</a></td><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=4">&gt;&gt;</a></td></tr></table></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1457-6</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos transversales</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Montt Moscoso, Alberto José (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2002-02-28</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1459-0</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos para tiritar de miedo</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Miranda Rojas, Paula (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2002-04-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1488-0</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos para tiritar de miedo</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Cardemil Herrera, Carmen (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2002-09-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1516-0</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos para tiritar de miedo (Obras escogidas)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Cardemil Herrera, Carmen (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2003-02-28</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1552-8</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Los hombres que hicieron llover</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2003-07-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>2</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1756-0</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>De miedos y pájaros (Obras Escogidas)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2006-01-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1757-7</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>De miedos y pájaros (Delfín de Color)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2006-01-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1760-7</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Mare Nostrum / Los seres vivos y su medio</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2006-02-28</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Inglés</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1761-4</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Mis padres son un huevo / La célula y su reproducción</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2006-02-28</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1842-0</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Los señores del átomo</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2007-02-28</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1896-3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Coseraut</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Ciencias naturales y Matemáticas</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2007-12-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1897-0</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos para adolescentes románticos</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura y retórica</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2008-03-05</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>16</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1898-7</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos para adolescentes románticos</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura y retórica</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2008-03-05</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>17</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1899-4</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Érase una vez un hermoso planeta llamado Tierra</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura y retórica</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2008-03-10</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>25</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1900-7</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Érase una vez un hermoso planeta llamado Tierra</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura y retórica</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2008-03-10</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>26</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr>  <tr>
    <td colspan="3">
      <table width="100%" class="titletable">
        <tr>
					<td><a href="buscador.php">Nueva b&uacute;squeda</a></td>
          <td>128 resultados encontrados.</td>
					<td align="center">P&aacute;gina 3 / 9</td>
					<td align="right"><table><tr><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=2">&lt;&lt;</a></td><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=4">&gt;&gt;</a></td></tr></table></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
</div>


<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" >
<title>Agencia ISBN :: Cámara Chilena del libro</title>
<script type="text/javascript" src="./script.js?nocache=1571096355"></script>
<link href="./ISBN_CSS.css" rel="stylesheet" type="text/css" >
<LINK REL="SHORTCUT ICON" HREF="./Imagenes/favicon.ico">

<style type="text/css">
<!--
select{
	border:#444444;
	border-style:solid;
	border-width:1px;
	font-family:Verdana, Arial, Helvetica, sans-serif;
	font-size:10px;
	color:#444444;
/*	display:block;	*/
}

#layerLogo {
	position:relative;
	left:65px;/*65*/
/*	top:61px;*/
	top:44px;
	width:250px;
	height:80px;
	z-index:4;
	background-image: url(./imagen.php?table=agencyparameter&field=logo&id=1);
}

#layerAdmin {
	position:relative;
	left:55px;
	top:474px;
	width:179px;
	height:133px;
	z-index:5;
}
#layerMenuTop {
	position:relative;
	left:62px;
	top:14px;
	width:866px;
	height:21px;
	z-index:6;
}
#layerMenuMiddle {
	position:relative;
	left:27px;
	top:147px;
	width:930px;
	height:10px;
	z-index:7;
}
#layerContForm {
	position:relative;
/*	width:100%;	*/
/*	height:100%;	*/
}
#layerCont {
	position:relative;
	left:20px;
	top:14px;
	width:946px;
	height:800px;
}
#footer {
	position:relative;
	left:280px;
	top:820px;
	width:482px;
	height:24px;
	z-index:8;
}
#menuAdmon {
	position:relative;
	left:175px;
	top:362px;
	width:580px;
	height:112px;
	z-index:10;
}
#LayerAgencia {
	position:relative;
	left:729px;
	top:76px;
	width:188px;
	height:52px;
	z-index:10;
	background-image: url(./Imagenes/IconBlackSmall.jpg);
}

-->
</style>
<style type="text/css">
.labelLogin {
	font:bold 11px Verdana, Arial, Helvetica, sans-serif;
}
#bannerHead {
	position:absolute;
	left:244px;
	top:20px;
	width:714px;
	height:125px;
	z-index:1;
	background-image: url(Imagenes/cabezote_isbn.jpg);
}

#menu {
/*width: 12em;*/
width: 100%;
}

#menu ul {
	list-style: none;
margin: 0;
padding: 0;
}

#menu a {
font: bold 11px/16px arial, helvetica, sans-serif;
display: block;
				 border-width: 1px;
				 border-style: solid;
				 border-color: #ccc #888 #555 #bbb;
margin: 0;
padding: 2px 3px;
}

#menu a {
	/*color: #000;*/
color: #fff;
			 /*background: #efefef;*/
background: #00246a;
						text-decoration: none;
}

#menu a:hover {
	/*color: #a00;
background: #fff;*/
background: #135AB0;
}

#menu li {
position: relative;
}

#menu ul ul ul {
position: absolute;
top: 0;
left: 100%;
width: 100%;
}

div#menu ul ul ul,
	div#menu ul ul li:hover ul ul
{display: none;}

div#menu ul ul li:hover ul,
	div#menu ul ul ul li:hover ul
{display: block;}

</style><!--[if IE]>

<style type="text/css" media="screen">

 #menu ul li {float: left; width: 100%;}

</style>

<![endif]--><!--[if lt IE 7]>

<style type="text/css" media="screen">

body {

behavior: url(csshover.htc);

					font-size: 100%;

} 

#menu ul li {float: left; width: 100%;}

#menu ul li a {height: 1%;} 



#menu a {

font: bold 9px arial, helvetica, sans-serif;

} 



</style>

<![endif]-->

<script type="text/javascript">
function show(_d)
{
  var _x = document.getElementById(_d);
 _x.style.visibility="visible";
}

function noShow(_d)
{
  var _x = document.getElementById(_d);
 _x.style.visibility="hidden";
}
-->
</script>
</head>
<body bgcolor="#FFFFFF">
<table align="center" width="930" border="0" cellpadding="0" cellspacing="0" style="height:100%">
	<tr>
		<td colspan="2">
			<table width="100%" cellpadding="0" cellspacing="0">
				<tr>
					<td height="125" valign="middle"><a href="http://www.camaradellibro.cl / www.isbnchile.cl"><img border="0" src="./imagen.php?table=agencyparameter&amp;field=logo&amp;id=1"></a></td>
					<td align="right">
											<img src="./Imagenes/IconBlackSmall.jpg">
										</td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td colspan="2">
			<table width="100%" cellpadding="0" cellspacing="0">
				<tr class="menuMiddle">
					<td bgcolor="#444444" width="20"></td>	
					<td bgcolor="#444444" height="20">
						Est&aacute; ubicado en: <a href="./login.php">Home</a>&nbsp;&rsaquo;&rsaquo;
						<a href="buscador.php">B&uacute;squeda de t&iacute;tulos</a>&nbsp;&rsaquo;&rsaquo; Resultados de la b&uacute;squeda					</td>
					<td bgcolor="#444444" onClick="closeSesion();" style="cursor:pointer;" align="right" width="112"><img src="./Imagenes/btnSesion.gif" width="112" height="19" align="middle"></td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td width="210" style="border: 1px solid #CCCCCC;" valign="top" align="center">
<div id="layerMenu">
	<table width="200">
		<tr><td align="center"><br><br><img src="Imagenes/searchLeft.jpg" width="77" height="428"></td></tr>
	</table>
</div>

		</td>
		<td style="border: 1px solid #CCCCCC;" valign="top">
<div id="layerContForm">
<br><br>
<table  width="500" border="0" align="center" cellpadding="0" cellspacing="2">
<tr><td colspan="3"><table width="100%" cellpadding="0" cellspacing="0" class="head_table"><tr><td bgcolor="#007520" NOWRAP>&nbsp;&rsaquo;&rsaquo;&nbsp;Resultados de la b&uacute;squeda&nbsp;&nbsp;</td><td width="17"><img src="Imagenes/imagen.php?icono=triangulo.png&amp;color=0,117,32"></td><td width="99%"><table width="100%" cellpadding="0" cellspacing="0"><tr><td height="16"></td></tr><tr><td height="3" style="background-image:url(Imagenes/imagen.php?icono=pixel.png&amp;color=0,117,32);"></td></tr></table></td></tr></table></td></tr>  <tr>
    <td colspan="3">
      <table width="100%" class="titletable">
        <tr>
					<td><a href="buscador.php">Nueva b&uacute;squeda</a></td>
          <td>128 resultados encontrados.</td>
					<td align="center">P&aacute;gina 4 / 9</td>
					<td align="right"><table><tr><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=3">&lt;&lt;</a></td><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=5">&gt;&gt;</a></td></tr></table></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1901-4</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Unos robots muy especiales</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura y retórica</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2008-03-07</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>4</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-1912-0</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Marcel y sus cuentos</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2008-07-23</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2104-8</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos de los derechos del niño</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2010-10-01</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>28</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2130-7</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos de los Derechos del Niño</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura chilena</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2010-12-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2547-3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>De miedos y pájaros</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2013-01-15</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>10</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2596-1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>El cazador de cuentos</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2013-08-05</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2597-8</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>El cazador de cuentos</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2013-08-05</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2598-5</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Antai</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2013-08-05</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2599-2</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Antai</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2013-08-05</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2611-1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>¿Quién mató a la tenquita?</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Cardemil Herrera, Carmen (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2013-08-19</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2613-5</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>De miedos y pájaros</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Jullian Fuentes, Pablo Andrés (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2013-10-07</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>11</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2615-9</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos de terror, de magia y de otras cosas extrañas</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Rodríguez Pérez, Verónica (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Narración de cuentos</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2013-08-22</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2616-6</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos de terror, de magia y de otras cosas extrañas</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Rodríguez Pérez, Verónica (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Narración de cuentos</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2013-09-23</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2650-0</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Érase un vez un hermoso planeta</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Jullian Fuentes, Pablo Andrés (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2013-12-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2681-4</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Marcel y sus cuentos</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Cifuentes, Claudio (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2014-01-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr>  <tr>
    <td colspan="3">
      <table width="100%" class="titletable">
        <tr>
					<td><a href="buscador.php">Nueva b&uacute;squeda</a></td>
          <td>128 resultados encontrados.</td>
					<td align="center">P&aacute;gina 4 / 9</td>
					<td align="right"><table><tr><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=3">&lt;&lt;</a></td><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=5">&gt;&gt;</a></td></tr></table></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
</div>


<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" >
<title>Agencia ISBN :: Cámara Chilena del libro</title>
<script type="text/javascript" src="./script.js?nocache=1470806783"></script>
<link href="./ISBN_CSS.css" rel="stylesheet" type="text/css" >
<LINK REL="SHORTCUT ICON" HREF="./Imagenes/favicon.ico">

<style type="text/css">
<!--
select{
	border:#444444;
	border-style:solid;
	border-width:1px;
	font-family:Verdana, Arial, Helvetica, sans-serif;
	font-size:10px;
	color:#444444;
/*	display:block;	*/
}

#layerLogo {
	position:relative;
	left:65px;/*65*/
/*	top:61px;*/
	top:44px;
	width:250px;
	height:80px;
	z-index:4;
	background-image: url(./imagen.php?table=agencyparameter&field=logo&id=1);
}

#layerAdmin {
	position:relative;
	left:55px;
	top:474px;
	width:179px;
	height:133px;
	z-index:5;
}
#layerMenuTop {
	position:relative;
	left:62px;
	top:14px;
	width:866px;
	height:21px;
	z-index:6;
}
#layerMenuMiddle {
	position:relative;
	left:27px;
	top:147px;
	width:930px;
	height:10px;
	z-index:7;
}
#layerContForm {
	position:relative;
/*	width:100%;	*/
/*	height:100%;	*/
}
#layerCont {
	position:relative;
	left:20px;
	top:14px;
	width:946px;
	height:800px;
}
#footer {
	position:relative;
	left:280px;
	top:820px;
	width:482px;
	height:24px;
	z-index:8;
}
#menuAdmon {
	position:relative;
	left:175px;
	top:362px;
	width:580px;
	height:112px;
	z-index:10;
}
#LayerAgencia {
	position:relative;
	left:729px;
	top:76px;
	width:188px;
	height:52px;
	z-index:10;
	background-image: url(./Imagenes/IconBlackSmall.jpg);
}

-->
</style>
<style type="text/css">
.labelLogin {
	font:bold 11px Verdana, Arial, Helvetica, sans-serif;
}
#bannerHead {
	position:absolute;
	left:244px;
	top:20px;
	width:714px;
	height:125px;
	z-index:1;
	background-image: url(Imagenes/cabezote_isbn.jpg);
}

#menu {
/*width: 12em;*/
width: 100%;
}

#menu ul {
	list-style: none;
margin: 0;
padding: 0;
}

#menu a {
font: bold 11px/16px arial, helvetica, sans-serif;
display: block;
				 border-width: 1px;
				 border-style: solid;
				 border-color: #ccc #888 #555 #bbb;
margin: 0;
padding: 2px 3px;
}

#menu a {
	/*color: #000;*/
color: #fff;
			 /*background: #efefef;*/
background: #00246a;
						text-decoration: none;
}

#menu a:hover {
	/*color: #a00;
background: #fff;*/
background: #135AB0;
}

#menu li {
position: relative;
}

#menu ul ul ul {
position: absolute;
top: 0;
left: 100%;
width: 100%;
}

div#menu ul ul ul,
	div#menu ul ul li:hover ul ul
{display: none;}

div#menu ul ul li:hover ul,
	div#menu ul ul ul li:hover ul
{display: block;}

</style><!--[if IE]>

<style type="text/css" media="screen">

 #menu ul li {float: left; width: 100%;}

</style>

<![endif]--><!--[if lt IE 7]>

<style type="text/css" media="screen">

body {

behavior: url(csshover.htc);

					font-size: 100%;

} 

#menu ul li {float: left; width: 100%;}

#menu ul li a {height: 1%;} 



#menu a {

font: bold 9px arial, helvetica, sans-serif;

} 



</style>

<![endif]-->

<script type="text/javascript">
function show(_d)
{
  var _x = document.getElementById(_d);
 _x.style.visibility="visible";
}

function noShow(_d)
{
  var _x = document.getElementById(_d);
 _x.style.visibility="hidden";
}
-->
</script>
</head>
<body bgcolor="#FFFFFF">
<table align="center" width="930" border="0" cellpadding="0" cellspacing="0" style="height:100%">
	<tr>
		<td colspan="2">
			<table width="100%" cellpadding="0" cellspacing="0">
				<tr>
					<td height="125" valign="middle"><a href="http://www.camaradellibro.cl / www.isbnchile.cl"><img border="0" src="./imagen.php?table=agencyparameter&amp;field=logo&amp;id=1"></a></td>
					<td align="right">
											<img src="./Imagenes/IconBlackSmall.jpg">
										</td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td colspan="2">
			<table width="100%" cellpadding="0" cellspacing="0">
				<tr class="menuMiddle">
					<td bgcolor="#444444" width="20"></td>	
					<td bgcolor="#444444" height="20">
						Est&aacute; ubicado en: <a href="./login.php">Home</a>&nbsp;&rsaquo;&rsaquo;
						<a href="buscador.php">B&uacute;squeda de t&iacute;tulos</a>&nbsp;&rsaquo;&rsaquo; Resultados de la b&uacute;squeda					</td>
					<td bgcolor="#444444" onClick="closeSesion();" style="cursor:pointer;" align="right" width="112"><img src="./Imagenes/btnSesion.gif" width="112" height="19" align="middle"></td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td width="210" style="border: 1px solid #CCCCCC;" valign="top" align="center">
<div id="layerMenu">
	<table width="200">
		<tr><td align="center"><br><br><img src="Imagenes/searchLeft.jpg" width="77" height="428"></td></tr>
	</table>
</div>

		</td>
		<td style="border: 1px solid #CCCCCC;" valign="top">
<div id="layerContForm">
<br><br>
<table  width="500" border="0" align="center" cellpadding="0" cellspacing="2">
<tr><td colspan="3"><table width="100%" cellpadding="0" cellspacing="0" class="head_table"><tr><td bgcolor="#007520" NOWRAP>&nbsp;&rsaquo;&rsaquo;&nbsp;Resultados de la b&uacute;squeda&nbsp;&nbsp;</td><td width="17"><img src="Imagenes/imagen.php?icono=triangulo.png&amp;color=0,117,32"></td><td width="99%"><table width="100%" cellpadding="0" cellspacing="0"><tr><td height="16"></td></tr><tr><td height="3" style="background-image:url(Imagenes/imagen.php?icono=pixel.png&amp;color=0,117,32);"></td></tr></table></td></tr></table></td></tr>  <tr>
    <td colspan="3">
      <table width="100%" class="titletable">
        <tr>
					<td><a href="buscador.php">Nueva b&uacute;squeda</a></td>
          <td>128 resultados encontrados.</td>
					<td align="center">P&aacute;gina 5 / 9</td>
					<td align="right"><table><tr><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=4">&lt;&lt;</a></td><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=6">&gt;&gt;</a></td></tr></table></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2712-5</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Antai, príncipe de los licanantai</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Frank Coloma, Marianela (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2014-03-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2713-2</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos de terror, de magia y de otras cosas extrañas</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Rodríguez Pérez, Verónica (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2014-03-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2873-3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>¿Quién mató a la tenquita?</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Cardemil Herrera, Carmen<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2016-02-01</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2942-6</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Antai, príncipe de los licanantai</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Frank Coloma, Marianela (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2016-09-05</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2943-3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>El cazador de cuentos</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Denis Arancibia, Carlos (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2016-09-05</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2944-0</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos de terror, de magia y de otras cosas extrañas</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Rodríguez Pérez, Verónica (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2016-09-12</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-2969-3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos de terror, de magia y de otras cosas extrañas</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Rodríguez Pérez, Verónica (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2016-10-24</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-3217-4</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Marcel y sus cuentos</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Cifuentes, Claudio (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2018-03-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-3221-1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos para tiritar de miedo</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2018-04-27</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-3330-0</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos para tiritar de miedo</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2018-09-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>27</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-3334-8</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos de los Derechos del Niño</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2018-09-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>44</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-3345-4</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos para sonreir</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2018-10-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>29</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-12-3347-8</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos para sonreír</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Zig-Zag S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2018-10-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-13-0997-5</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>El cazador de cuentos</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Gerber, Thomas (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Andrés Bello</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1992-03-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Inglés</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-13-1066-7</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Tres príncipes</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Gerber, Thomas (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Andrés Bello</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1993-03-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Francés</td></tr>
<tr><td colspan="2">-------</td></tr>  <tr>
    <td colspan="3">
      <table width="100%" class="titletable">
        <tr>
					<td><a href="buscador.php">Nueva b&uacute;squeda</a></td>
          <td>128 resultados encontrados.</td>
					<td align="center">P&aacute;gina 5 / 9</td>
					<td align="right"><table><tr><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=4">&lt;&lt;</a></td><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=6">&gt;&gt;</a></td></tr></table></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
</div>


<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" >
<title>Agencia ISBN :: Cámara Chilena del libro</title>
<script type="text/javascript" src="./script.js?nocache=2084343696"></script>
<link href="./ISBN_CSS.css" rel="stylesheet" type="text/css" >
<LINK REL="SHORTCUT ICON" HREF="./Imagenes/favicon.ico">

<style type="text/css">
<!--
select{
	border:#444444;
	border-style:solid;
	border-width:1px;
	font-family:Verdana, Arial, Helvetica, sans-serif;
	font-size:10px;
	color:#444444;
/*	display:block;	*/
}

#layerLogo {
	position:relative;
	left:65px;/*65*/
/*	top:61px;*/
	top:44px;
	width:250px;
	height:80px;
	z-index:4;
	background-image: url(./imagen.php?table=agencyparameter&field=logo&id=1);
}

#layerAdmin {
	position:relative;
	left:55px;
	top:474px;
	width:179px;
	height:133px;
	z-index:5;
}
#layerMenuTop {
	position:relative;
	left:62px;
	top:14px;
	width:866px;
	height:21px;
	z-index:6;
}
#layerMenuMiddle {
	position:relative;
	left:27px;
	top:147px;
	width:930px;
	height:10px;
	z-index:7;
}
#layerContForm {
	position:relative;
/*	width:100%;	*/
/*	height:100%;	*/
}
#layerCont {
	position:relative;
	left:20px;
	top:14px;
	width:946px;
	height:800px;
}
#footer {
	position:relative;
	left:280px;
	top:820px;
	width:482px;
	height:24px;
	z-index:8;
}
#menuAdmon {
	position:relative;
	left:175px;
	top:362px;
	width:580px;
	height:112px;
	z-index:10;
}
#LayerAgencia {
	position:relative;
	left:729px;
	top:76px;
	width:188px;
	height:52px;
	z-index:10;
	background-image: url(./Imagenes/IconBlackSmall.jpg);
}

-->
</style>
<style type="text/css">
.labelLogin {
	font:bold 11px Verdana, Arial, Helvetica, sans-serif;
}
#bannerHead {
	position:absolute;
	left:244px;
	top:20px;
	width:714px;
	height:125px;
	z-index:1;
	background-image: url(Imagenes/cabezote_isbn.jpg);
}

#menu {
/*width: 12em;*/
width: 100%;
}

#menu ul {
	list-style: none;
margin: 0;
padding: 0;
}

#menu a {
font: bold 11px/16px arial, helvetica, sans-serif;
display: block;
				 border-width: 1px;
				 border-style: solid;
				 border-color: #ccc #888 #555 #bbb;
margin: 0;
padding: 2px 3px;
}

#menu a {
	/*color: #000;*/
color: #fff;
			 /*background: #efefef;*/
background: #00246a;
						text-decoration: none;
}

#menu a:hover {
	/*color: #a00;
background: #fff;*/
background: #135AB0;
}

#menu li {
position: relative;
}

#menu ul ul ul {
position: absolute;
top: 0;
left: 100%;
width: 100%;
}

div#menu ul ul ul,
	div#menu ul ul li:hover ul ul
{display: none;}

div#menu ul ul li:hover ul,
	div#menu ul ul ul li:hover ul
{display: block;}

</style><!--[if IE]>

<style type="text/css" media="screen">

 #menu ul li {float: left; width: 100%;}

</style>

<![endif]--><!--[if lt IE 7]>

<style type="text/css" media="screen">

body {

behavior: url(csshover.htc);

					font-size: 100%;

} 

#menu ul li {float: left; width: 100%;}

#menu ul li a {height: 1%;} 



#menu a {

font: bold 9px arial, helvetica, sans-serif;

} 



</style>

<![endif]-->

<script type="text/javascript">
function show(_d)
{
  var _x = document.getElementById(_d);
 _x.style.visibility="visible";
}

function noShow(_d)
{
  var _x = document.getElementById(_d);
 _x.style.visibility="hidden";
}
-->
</script>
</head>
<body bgcolor="#FFFFFF">
<table align="center" width="930" border="0" cellpadding="0" cellspacing="0" style="height:100%">
	<tr>
		<td colspan="2">
			<table width="100%" cellpadding="0" cellspacing="0">
				<tr>
					<td height="125" valign="middle"><a href="http://www.camaradellibro.cl / www.isbnchile.cl"><img border="0" src="./imagen.php?table=agencyparameter&amp;field=logo&amp;id=1"></a></td>
					<td align="right">
											<img src="./Imagenes/IconBlackSmall.jpg">
										</td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td colspan="2">
			<table width="100%" cellpadding="0" cellspacing="0">
				<tr class="menuMiddle">
					<td bgcolor="#444444" width="20"></td>	
					<td bgcolor="#444444" height="20">
						Est&aacute; ubicado en: <a href="./login.php">Home</a>&nbsp;&rsaquo;&rsaquo;
						<a href="buscador.php">B&uacute;squeda de t&iacute;tulos</a>&nbsp;&rsaquo;&rsaquo; Resultados de la b&uacute;squeda					</td>
					<td bgcolor="#444444" onClick="closeSesion();" style="cursor:pointer;" align="right" width="112"><img src="./Imagenes/btnSesion.gif" width="112" height="19" align="middle"></td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td width="210" style="border: 1px solid #CCCCCC;" valign="top" align="center">
<div id="layerMenu">
	<table width="200">
		<tr><td align="center"><br><br><img src="Imagenes/searchLeft.jpg" width="77" height="428"></td></tr>
	</table>
</div>

		</td>
		<td style="border: 1px solid #CCCCCC;" valign="top">
<div id="layerContForm">
<br><br>
<table  width="500" border="0" align="center" cellpadding="0" cellspacing="2">
<tr><td colspan="3"><table width="100%" cellpadding="0" cellspacing="0" class="head_table"><tr><td bgcolor="#007520" NOWRAP>&nbsp;&rsaquo;&rsaquo;&nbsp;Resultados de la b&uacute;squeda&nbsp;&nbsp;</td><td width="17"><img src="Imagenes/imagen.php?icono=triangulo.png&amp;color=0,117,32"></td><td width="99%"><table width="100%" cellpadding="0" cellspacing="0"><tr><td height="16"></td></tr><tr><td height="3" style="background-image:url(Imagenes/imagen.php?icono=pixel.png&amp;color=0,117,32);"></td></tr></table></td></tr></table></td></tr>  <tr>
    <td colspan="3">
      <table width="100%" class="titletable">
        <tr>
					<td><a href="buscador.php">Nueva b&uacute;squeda</a></td>
          <td>128 resultados encontrados.</td>
					<td align="center">P&aacute;gina 6 / 9</td>
					<td align="right"><table><tr><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=5">&lt;&lt;</a></td><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=7">&gt;&gt;</a></td></tr></table></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-13-1248-7</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Teatro infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Campos Ordenes, Natacha (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Andrés Bello</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Teatro chileno</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1994-08-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Inglés</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-13-1319-4</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos de terror, de magia y de otras cosas extrañas</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Castell Rey, Antonio (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Andrés Bello</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1995-07-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Inglés</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-13-1337-8</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Upapapá</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Campos Ordenes, Natacha (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Andrés Bello</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1995-10-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-13-1398-9</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Descubrimiento</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Campos Ordenes, Natacha (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Andrés Bello</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1996-04-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Inglés</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-13-1399-6</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Mi hermano Daniel</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Campos Ordenes, Natacha (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Andrés Bello</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1996-04-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-13-1740-6</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Del Cuzco al Cachapoal</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Andrés Bello</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2001-11-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-16-0227-4</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Guakolda y Lautaro</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Pehuén Editores S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1997-05-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Francés</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-18-0600-9</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>¿Quieren saber por qué les cuento cuentos Yámanas?</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Miranda Zamora, Carlos (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Don Bosco - Chile Editorial</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2003-03-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-18-0683-2</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>¿Quieren saber por qué les cuento cuentos aymarás?</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Miranda Zamora, Carlos (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Don Bosco - Chile Editorial</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2004-05-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-18-0711-2</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>¿Quieren saber por qué les cuento cuentos RapaNui?</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Miranda Zamora, Carlos (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Don Bosco - Chile Editorial</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2005-04-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-18-0730-3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>¿Quieren saber por qué les cuento cuentos mapuches?</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Miranda Zamora, Carlos (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Don Bosco - Chile Editorial</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2006-08-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-18-0755-6</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>¿Quieren saber por qué les cuento cuentos Aónikenk?</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Don Bosco - Chile Editorial</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2007-04-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-18-0770-9</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Manolito Bostezos y otros niños modelo</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Gormaz Vargas, Viviana (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Don Bosco - Chile Editorial</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2007-09-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-18-0825-6</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>La tucúquere</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Don Bosco - Chile Editorial</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2012-06-01</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-18-0828-7</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>La princesa Murta</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Don Bosco - Chile Editorial</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2012-06-01</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr>  <tr>
    <td colspan="3">
      <table width="100%" class="titletable">
        <tr>
					<td><a href="buscador.php">Nueva b&uacute;squeda</a></td>
          <td>128 resultados encontrados.</td>
					<td align="center">P&aacute;gina 6 / 9</td>
					<td align="right"><table><tr><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=5">&lt;&lt;</a></td><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=7">&gt;&gt;</a></td></tr></table></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
</div>


<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" >
<title>Agencia ISBN :: Cámara Chilena del libro</title>
<script type="text/javascript" src="./script.js?nocache=1852201622"></script>
<link href="./ISBN_CSS.css" rel="stylesheet" type="text/css" >
<LINK REL="SHORTCUT ICON" HREF="./Imagenes/favicon.ico">

<style type="text/css">
<!--
select{
	border:#444444;
	border-style:solid;
	border-width:1px;
	font-family:Verdana, Arial, Helvetica, sans-serif;
	font-size:10px;
	color:#444444;
/*	display:block;	*/
}

#layerLogo {
	position:relative;
	left:65px;/*65*/
/*	top:61px;*/
	top:44px;
	width:250px;
	height:80px;
	z-index:4;
	background-image: url(./imagen.php?table=agencyparameter&field=logo&id=1);
}

#layerAdmin {
	position:relative;
	left:55px;
	top:474px;
	width:179px;
	height:133px;
	z-index:5;
}
#layerMenuTop {
	position:relative;
	left:62px;
	top:14px;
	width:866px;
	height:21px;
	z-index:6;
}
#layerMenuMiddle {
	position:relative;
	left:27px;
	top:147px;
	width:930px;
	height:10px;
	z-index:7;
}
#layerContForm {
	position:relative;
/*	width:100%;	*/
/*	height:100%;	*/
}
#layerCont {
	position:relative;
	left:20px;
	top:14px;
	width:946px;
	height:800px;
}
#footer {
	position:relative;
	left:280px;
	top:820px;
	width:482px;
	height:24px;
	z-index:8;
}
#menuAdmon {
	position:relative;
	left:175px;
	top:362px;
	width:580px;
	height:112px;
	z-index:10;
}
#LayerAgencia {
	position:relative;
	left:729px;
	top:76px;
	width:188px;
	height:52px;
	z-index:10;
	background-image: url(./Imagenes/IconBlackSmall.jpg);
}

-->
</style>
<style type="text/css">
.labelLogin {
	font:bold 11px Verdana, Arial, Helvetica, sans-serif;
}
#bannerHead {
	position:absolute;
	left:244px;
	top:20px;
	width:714px;
	height:125px;
	z-index:1;
	background-image: url(Imagenes/cabezote_isbn.jpg);
}

#menu {
/*width: 12em;*/
width: 100%;
}

#menu ul {
	list-style: none;
margin: 0;
padding: 0;
}

#menu a {
font: bold 11px/16px arial, helvetica, sans-serif;
display: block;
				 border-width: 1px;
				 border-style: solid;
				 border-color: #ccc #888 #555 #bbb;
margin: 0;
padding: 2px 3px;
}

#menu a {
	/*color: #000;*/
color: #fff;
			 /*background: #efefef;*/
background: #00246a;
						text-decoration: none;
}

#menu a:hover {
	/*color: #a00;
background: #fff;*/
background: #135AB0;
}

#menu li {
position: relative;
}

#menu ul ul ul {
position: absolute;
top: 0;
left: 100%;
width: 100%;
}

div#menu ul ul ul,
	div#menu ul ul li:hover ul ul
{display: none;}

div#menu ul ul li:hover ul,
	div#menu ul ul ul li:hover ul
{display: block;}

</style><!--[if IE]>

<style type="text/css" media="screen">

 #menu ul li {float: left; width: 100%;}

</style>

<![endif]--><!--[if lt IE 7]>

<style type="text/css" media="screen">

body {

behavior: url(csshover.htc);

					font-size: 100%;

} 

#menu ul li {float: left; width: 100%;}

#menu ul li a {height: 1%;} 



#menu a {

font: bold 9px arial, helvetica, sans-serif;

} 



</style>

<![endif]-->

<script type="text/javascript">
function show(_d)
{
  var _x = document.getElementById(_d);
 _x.style.visibility="visible";
}

function noShow(_d)
{
  var _x = document.getElementById(_d);
 _x.style.visibility="hidden";
}
-->
</script>
</head>
<body bgcolor="#FFFFFF">
<table align="center" width="930" border="0" cellpadding="0" cellspacing="0" style="height:100%">
	<tr>
		<td colspan="2">
			<table width="100%" cellpadding="0" cellspacing="0">
				<tr>
					<td height="125" valign="middle"><a href="http://www.camaradellibro.cl / www.isbnchile.cl"><img border="0" src="./imagen.php?table=agencyparameter&amp;field=logo&amp;id=1"></a></td>
					<td align="right">
											<img src="./Imagenes/IconBlackSmall.jpg">
										</td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td colspan="2">
			<table width="100%" cellpadding="0" cellspacing="0">
				<tr class="menuMiddle">
					<td bgcolor="#444444" width="20"></td>	
					<td bgcolor="#444444" height="20">
						Est&aacute; ubicado en: <a href="./login.php">Home</a>&nbsp;&rsaquo;&rsaquo;
						<a href="buscador.php">B&uacute;squeda de t&iacute;tulos</a>&nbsp;&rsaquo;&rsaquo; Resultados de la b&uacute;squeda					</td>
					<td bgcolor="#444444" onClick="closeSesion();" style="cursor:pointer;" align="right" width="112"><img src="./Imagenes/btnSesion.gif" width="112" height="19" align="middle"></td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td width="210" style="border: 1px solid #CCCCCC;" valign="top" align="center">
<div id="layerMenu">
	<table width="200">
		<tr><td align="center"><br><br><img src="Imagenes/searchLeft.jpg" width="77" height="428"></td></tr>
	</table>
</div>

		</td>
		<td style="border: 1px solid #CCCCCC;" valign="top">
<div id="layerContForm">
<br><br>
<table  width="500" border="0" align="center" cellpadding="0" cellspacing="2">
<tr><td colspan="3"><table width="100%" cellpadding="0" cellspacing="0" class="head_table"><tr><td bgcolor="#007520" NOWRAP>&nbsp;&rsaquo;&rsaquo;&nbsp;Resultados de la b&uacute;squeda&nbsp;&nbsp;</td><td width="17"><img src="Imagenes/imagen.php?icono=triangulo.png&amp;color=0,117,32"></td><td width="99%"><table width="100%" cellpadding="0" cellspacing="0"><tr><td height="16"></td></tr><tr><td height="3" style="background-image:url(Imagenes/imagen.php?icono=pixel.png&amp;color=0,117,32);"></td></tr></table></td></tr></table></td></tr>  <tr>
    <td colspan="3">
      <table width="100%" class="titletable">
        <tr>
					<td><a href="buscador.php">Nueva b&uacute;squeda</a></td>
          <td>128 resultados encontrados.</td>
					<td align="center">P&aacute;gina 7 / 9</td>
					<td align="right"><table><tr><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=6">&lt;&lt;</a></td><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=8">&gt;&gt;</a></td></tr></table></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-18-0831-7</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>La leyenda de las estrellas</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Don Bosco - Chile Editorial</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2012-06-01</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-18-0841-6</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Manolito Bostezos y otros niños modelo</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Don Bosco - Chile Editorial</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura y retórica</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2013-05-27</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-18-0845-4</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Manolito Bostezos y otros niños modelo</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl (Adaptador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Don Bosco - Chile Editorial</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2013-05-28</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-18-0930-7</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Láminas La princesa Murta</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Equipo Editorial Edebé (Adaptador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Don Bosco - Chile Editorial</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura y retórica</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2014-11-25</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-18-1013-6</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos con pulgas</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Pérez Bustos, Leonor Alejandra (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Don Bosco - Chile Editorial</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2017-03-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-18-1070-9</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Poemas para volar</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Pérez Bustos, Leonor Alejandra (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Don Bosco - Chile Editorial</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2017-10-24</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-18-1177-5</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>La leyenda de las estrellas</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Leppe Gnecco, Leslie Paulina (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Don Bosco - Chile Editorial</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2019-07-17</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-19-0463-7</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>De la diversidad de gentes</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Estrella Avila, Jorge<br>Schkolnik, Samuel</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Universidad de Chile</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura argentina</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2005-05-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-240-214-9</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos con pulgas</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Castell Rey, Antonio (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Arrayán Editores S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1997-04-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-240-272-9</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Poemas para volar</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Arrayán Editores S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Poesía chilena</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1999-08-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-249-219-5</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Un extraño globo</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Loyola M., Anisol (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Salo S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1993-09-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-249-273-7</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Piri el gusanito</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Castell Rey, Antonio (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Salo S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1994-10-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-249-276-8</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>La princesa Murta</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Castell Rey, Antonio (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Salo S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1994-10-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-249-282-9</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>El mejor cazador</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Castell Rey, Antonio (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Salo S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1994-12-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-249-283-6</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Rayén y Llacolén</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Castell Rey, Antonio (Ilustrador)<br>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Salo S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1994-12-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr>  <tr>
    <td colspan="3">
      <table width="100%" class="titletable">
        <tr>
					<td><a href="buscador.php">Nueva b&uacute;squeda</a></td>
          <td>128 resultados encontrados.</td>
					<td align="center">P&aacute;gina 7 / 9</td>
					<td align="right"><table><tr><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=6">&lt;&lt;</a></td><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=8">&gt;&gt;</a></td></tr></table></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
</div>


<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" >
<title>Agencia ISBN :: Cámara Chilena del libro</title>
<script type="text/javascript" src="./script.js?nocache=86181620"></script>
<link href="./ISBN_CSS.css" rel="stylesheet" type="text/css" >
<LINK REL="SHORTCUT ICON" HREF="./Imagenes/favicon.ico">

<style type="text/css">
<!--
select{
	border:#444444;
	border-style:solid;
	border-width:1px;
	font-family:Verdana, Arial, Helvetica, sans-serif;
	font-size:10px;
	color:#444444;
/*	display:block;	*/
}

#layerLogo {
	position:relative;
	left:65px;/*65*/
/*	top:61px;*/
	top:44px;
	width:250px;
	height:80px;
	z-index:4;
	background-image: url(./imagen.php?table=agencyparameter&field=logo&id=1);
}

#layerAdmin {
	position:relative;
	left:55px;
	top:474px;
	width:179px;
	height:133px;
	z-index:5;
}
#layerMenuTop {
	position:relative;
	left:62px;
	top:14px;
	width:866px;
	height:21px;
	z-index:6;
}
#layerMenuMiddle {
	position:relative;
	left:27px;
	top:147px;
	width:930px;
	height:10px;
	z-index:7;
}
#layerContForm {
	position:relative;
/*	width:100%;	*/
/*	height:100%;	*/
}
#layerCont {
	position:relative;
	left:20px;
	top:14px;
	width:946px;
	height:800px;
}
#footer {
	position:relative;
	left:280px;
	top:820px;
	width:482px;
	height:24px;
	z-index:8;
}
#menuAdmon {
	position:relative;
	left:175px;
	top:362px;
	width:580px;
	height:112px;
	z-index:10;
}
#LayerAgencia {
	position:relative;
	left:729px;
	top:76px;
	width:188px;
	height:52px;
	z-index:10;
	background-image: url(./Imagenes/IconBlackSmall.jpg);
}

-->
</style>
<style type="text/css">
.labelLogin {
	font:bold 11px Verdana, Arial, Helvetica, sans-serif;
}
#bannerHead {
	position:absolute;
	left:244px;
	top:20px;
	width:714px;
	height:125px;
	z-index:1;
	background-image: url(Imagenes/cabezote_isbn.jpg);
}

#menu {
/*width: 12em;*/
width: 100%;
}

#menu ul {
	list-style: none;
margin: 0;
padding: 0;
}

#menu a {
font: bold 11px/16px arial, helvetica, sans-serif;
display: block;
				 border-width: 1px;
				 border-style: solid;
				 border-color: #ccc #888 #555 #bbb;
margin: 0;
padding: 2px 3px;
}

#menu a {
	/*color: #000;*/
color: #fff;
			 /*background: #efefef;*/
background: #00246a;
						text-decoration: none;
}

#menu a:hover {
	/*color: #a00;
background: #fff;*/
background: #135AB0;
}

#menu li {
position: relative;
}

#menu ul ul ul {
position: absolute;
top: 0;
left: 100%;
width: 100%;
}

div#menu ul ul ul,
	div#menu ul ul li:hover ul ul
{display: none;}

div#menu ul ul li:hover ul,
	div#menu ul ul ul li:hover ul
{display: block;}

</style><!--[if IE]>

<style type="text/css" media="screen">

 #menu ul li {float: left; width: 100%;}

</style>

<![endif]--><!--[if lt IE 7]>

<style type="text/css" media="screen">

body {

behavior: url(csshover.htc);

					font-size: 100%;

} 

#menu ul li {float: left; width: 100%;}

#menu ul li a {height: 1%;} 



#menu a {

font: bold 9px arial, helvetica, sans-serif;

} 



</style>

<![endif]-->

<script type="text/javascript">
function show(_d)
{
  var _x = document.getElementById(_d);
 _x.style.visibility="visible";
}

function noShow(_d)
{
  var _x = document.getElementById(_d);
 _x.style.visibility="hidden";
}
-->
</script>
</head>
<body bgcolor="#FFFFFF">
<table align="center" width="930" border="0" cellpadding="0" cellspacing="0" style="height:100%">
	<tr>
		<td colspan="2">
			<table width="100%" cellpadding="0" cellspacing="0">
				<tr>
					<td height="125" valign="middle"><a href="http://www.camaradellibro.cl / www.isbnchile.cl"><img border="0" src="./imagen.php?table=agencyparameter&amp;field=logo&amp;id=1"></a></td>
					<td align="right">
											<img src="./Imagenes/IconBlackSmall.jpg">
										</td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td colspan="2">
			<table width="100%" cellpadding="0" cellspacing="0">
				<tr class="menuMiddle">
					<td bgcolor="#444444" width="20"></td>	
					<td bgcolor="#444444" height="20">
						Est&aacute; ubicado en: <a href="./login.php">Home</a>&nbsp;&rsaquo;&rsaquo;
						<a href="buscador.php">B&uacute;squeda de t&iacute;tulos</a>&nbsp;&rsaquo;&rsaquo; Resultados de la b&uacute;squeda					</td>
					<td bgcolor="#444444" onClick="closeSesion();" style="cursor:pointer;" align="right" width="112"><img src="./Imagenes/btnSesion.gif" width="112" height="19" align="middle"></td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td width="210" style="border: 1px solid #CCCCCC;" valign="top" align="center">
<div id="layerMenu">
	<table width="200">
		<tr><td align="center"><br><br><img src="Imagenes/searchLeft.jpg" width="77" height="428"></td></tr>
	</table>
</div>

		</td>
		<td style="border: 1px solid #CCCCCC;" valign="top">
<div id="layerContForm">
<br><br>
<table  width="500" border="0" align="center" cellpadding="0" cellspacing="2">
<tr><td colspan="3"><table width="100%" cellpadding="0" cellspacing="0" class="head_table"><tr><td bgcolor="#007520" NOWRAP>&nbsp;&rsaquo;&rsaquo;&nbsp;Resultados de la b&uacute;squeda&nbsp;&nbsp;</td><td width="17"><img src="Imagenes/imagen.php?icono=triangulo.png&amp;color=0,117,32"></td><td width="99%"><table width="100%" cellpadding="0" cellspacing="0"><tr><td height="16"></td></tr><tr><td height="3" style="background-image:url(Imagenes/imagen.php?icono=pixel.png&amp;color=0,117,32);"></td></tr></table></td></tr></table></td></tr>  <tr>
    <td colspan="3">
      <table width="100%" class="titletable">
        <tr>
					<td><a href="buscador.php">Nueva b&uacute;squeda</a></td>
          <td>128 resultados encontrados.</td>
					<td align="center">P&aacute;gina 8 / 9</td>
					<td align="right"><table><tr><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=7">&lt;&lt;</a></td><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=9">&gt;&gt;</a></td></tr></table></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-249-699-5</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>La ciudad en la botella</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Salo S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2005-06-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-249-700-8</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Qué hago con el sitio de al lado de mi casa</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Salo S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2005-06-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-264-100-5</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Breve noticia de mi infancia</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>SM S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1998-12-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-264-129-6</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>¿Hacia dónde volarán los pajaros?</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Loyola M., Anisol (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>SM S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1999-11-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-264-223-1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>No me creas lo que te cuento</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>SM S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura chilena</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2003-10-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-264-484-6</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Un mundo de lectura</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Hojas Loret, Isabel Margarita (Ilustrador)<br>Arteaga Jarrett, Isidro (Ilustrador)<br>Lungenstrass Alvarez, Christian (Ilustrador)<br>Jullian Fuentes, Pablo Andrés (Ilustrador)<br>Peña Muñoz, Manuel<br>Marty Aboitiz de Balcells, Jacqueline<br>Schkolnik Bendersky, Saúl<br>Hidalgo González, Héctor<br>Güiraldes Camerati, Ana María<br>Hertling, Gisella<br>Soto Seidemann, María de la Luz<br>Alliende González, Felipe<br>Condemarín Grimberg, Mabel<br>Morel Chaigneau, Alicia</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>SM S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2007-12-03</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-289-141-7</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos ecológicos</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Fondo de Cultura Económica Chile S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2016-06-01</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-289-166-0</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Viaje mágico a Chiloé</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Montt Moscoso, Alberto José (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Fondo de Cultura Económica Chile S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2017-11-01</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-294-097-9</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Los siete días de la creación</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Moya Vega, René (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>MN Editorial Ltda.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2005-06-30</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-294-278-2</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos con pulgas</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>MN Editorial Ltda.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2010-06-15</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-294-280-5</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Poemas para volar</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>MN Editorial Ltda.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2010-06-15</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-300-043-6</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Un extraño globo. La ratona Petronila</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Suárez Torres, María Emilia (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Editorial Norma de Chile</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2005-10-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-300-115-0</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Lucía intrusas. Manolito bostezos</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Editorial Norma de Chile</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2007-05-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-324-289-8</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Petra radius</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Editorial Catalonia Ltda.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2014-05-26</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-324-306-2</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Petra radius</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Editorial Catalonia Ltda.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2014-06-24</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr>  <tr>
    <td colspan="3">
      <table width="100%" class="titletable">
        <tr>
					<td><a href="buscador.php">Nueva b&uacute;squeda</a></td>
          <td>128 resultados encontrados.</td>
					<td align="center">P&aacute;gina 8 / 9</td>
					<td align="right"><table><tr><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=7">&lt;&lt;</a></td><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=9">&gt;&gt;</a></td></tr></table></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
</div>


<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" >
<title>Agencia ISBN :: Cámara Chilena del libro</title>
<script type="text/javascript" src="./script.js?nocache=353927834"></script>
<link href="./ISBN_CSS.css" rel="stylesheet" type="text/css" >
<LINK REL="SHORTCUT ICON" HREF="./Imagenes/favicon.ico">

<style type="text/css">
<!--
select{
	border:#444444;
	border-style:solid;
	border-width:1px;
	font-family:Verdana, Arial, Helvetica, sans-serif;
	font-size:10px;
	color:#444444;
/*	display:block;	*/
}

#layerLogo {
	position:relative;
	left:65px;/*65*/
/*	top:61px;*/
	top:44px;
	width:250px;
	height:80px;
	z-index:4;
	background-image: url(./imagen.php?table=agencyparameter&field=logo&id=1);
}

#layerAdmin {
	position:relative;
	left:55px;
	top:474px;
	width:179px;
	height:133px;
	z-index:5;
}
#layerMenuTop {
	position:relative;
	left:62px;
	top:14px;
	width:866px;
	height:21px;
	z-index:6;
}
#layerMenuMiddle {
	position:relative;
	left:27px;
	top:147px;
	width:930px;
	height:10px;
	z-index:7;
}
#layerContForm {
	position:relative;
/*	width:100%;	*/
/*	height:100%;	*/
}
#layerCont {
	position:relative;
	left:20px;
	top:14px;
	width:946px;
	height:800px;
}
#footer {
	position:relative;
	left:280px;
	top:820px;
	width:482px;
	height:24px;
	z-index:8;
}
#menuAdmon {
	position:relative;
	left:175px;
	top:362px;
	width:580px;
	height:112px;
	z-index:10;
}
#LayerAgencia {
	position:relative;
	left:729px;
	top:76px;
	width:188px;
	height:52px;
	z-index:10;
	background-image: url(./Imagenes/IconBlackSmall.jpg);
}

-->
</style>
<style type="text/css">
.labelLogin {
	font:bold 11px Verdana, Arial, Helvetica, sans-serif;
}
#bannerHead {
	position:absolute;
	left:244px;
	top:20px;
	width:714px;
	height:125px;
	z-index:1;
	background-image: url(Imagenes/cabezote_isbn.jpg);
}

#menu {
/*width: 12em;*/
width: 100%;
}

#menu ul {
	list-style: none;
margin: 0;
padding: 0;
}

#menu a {
font: bold 11px/16px arial, helvetica, sans-serif;
display: block;
				 border-width: 1px;
				 border-style: solid;
				 border-color: #ccc #888 #555 #bbb;
margin: 0;
padding: 2px 3px;
}

#menu a {
	/*color: #000;*/
color: #fff;
			 /*background: #efefef;*/
background: #00246a;
						text-decoration: none;
}

#menu a:hover {
	/*color: #a00;
background: #fff;*/
background: #135AB0;
}

#menu li {
position: relative;
}

#menu ul ul ul {
position: absolute;
top: 0;
left: 100%;
width: 100%;
}

div#menu ul ul ul,
	div#menu ul ul li:hover ul ul
{display: none;}

div#menu ul ul li:hover ul,
	div#menu ul ul ul li:hover ul
{display: block;}

</style><!--[if IE]>

<style type="text/css" media="screen">

 #menu ul li {float: left; width: 100%;}

</style>

<![endif]--><!--[if lt IE 7]>

<style type="text/css" media="screen">

body {

behavior: url(csshover.htc);

					font-size: 100%;

} 

#menu ul li {float: left; width: 100%;}

#menu ul li a {height: 1%;} 



#menu a {

font: bold 9px arial, helvetica, sans-serif;

} 



</style>

<![endif]-->

<script type="text/javascript">
function show(_d)
{
  var _x = document.getElementById(_d);
 _x.style.visibility="visible";
}

function noShow(_d)
{
  var _x = document.getElementById(_d);
 _x.style.visibility="hidden";
}
-->
</script>
</head>
<body bgcolor="#FFFFFF">
<table align="center" width="930" border="0" cellpadding="0" cellspacing="0" style="height:100%">
	<tr>
		<td colspan="2">
			<table width="100%" cellpadding="0" cellspacing="0">
				<tr>
					<td height="125" valign="middle"><a href="http://www.camaradellibro.cl / www.isbnchile.cl"><img border="0" src="./imagen.php?table=agencyparameter&amp;field=logo&amp;id=1"></a></td>
					<td align="right">
											<img src="./Imagenes/IconBlackSmall.jpg">
										</td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td colspan="2">
			<table width="100%" cellpadding="0" cellspacing="0">
				<tr class="menuMiddle">
					<td bgcolor="#444444" width="20"></td>	
					<td bgcolor="#444444" height="20">
						Est&aacute; ubicado en: <a href="./login.php">Home</a>&nbsp;&rsaquo;&rsaquo;
						<a href="buscador.php">B&uacute;squeda de t&iacute;tulos</a>&nbsp;&rsaquo;&rsaquo; Resultados de la b&uacute;squeda					</td>
					<td bgcolor="#444444" onClick="closeSesion();" style="cursor:pointer;" align="right" width="112"><img src="./Imagenes/btnSesion.gif" width="112" height="19" align="middle"></td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td width="210" style="border: 1px solid #CCCCCC;" valign="top" align="center">
<div id="layerMenu">
	<table width="200">
		<tr><td align="center"><br><br><img src="Imagenes/searchLeft.jpg" width="77" height="428"></td></tr>
	</table>
</div>

		</td>
		<td style="border: 1px solid #CCCCCC;" valign="top">
<div id="layerContForm">
<br><br>
<table  width="500" border="0" align="center" cellpadding="0" cellspacing="2">
<tr><td colspan="3"><table width="100%" cellpadding="0" cellspacing="0" class="head_table"><tr><td bgcolor="#007520" NOWRAP>&nbsp;&rsaquo;&rsaquo;&nbsp;Resultados de la b&uacute;squeda&nbsp;&nbsp;</td><td width="17"><img src="Imagenes/imagen.php?icono=triangulo.png&amp;color=0,117,32"></td><td width="99%"><table width="100%" cellpadding="0" cellspacing="0"><tr><td height="16"></td></tr><tr><td height="3" style="background-image:url(Imagenes/imagen.php?icono=pixel.png&amp;color=0,117,32);"></td></tr></table></td></tr></table></td></tr>  <tr>
    <td colspan="3">
      <table width="100%" class="titletable">
        <tr>
					<td><a href="buscador.php">Nueva b&uacute;squeda</a></td>
          <td>128 resultados encontrados.</td>
					<td align="center">P&aacute;gina 9 / 9</td>
					<td align="right"><table><tr><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=8">&lt;&lt;</a></td><td>&gt;&gt;</td></tr></table></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-324-555-4</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Petra radius</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Editorial Catalonia Ltda.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2017-11-29</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-351-308-0</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>El juego de escribir</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Educación. investigación. temas relacionados con la literatura</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2012-07-16</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-7083-49-7</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>El ratón forzudo y el resorte</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Cardemil Herrera, Carmen (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Fondo de Cultura Económica S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1996-01-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Inglés</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-7083-50-3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Cuentos ecológicos</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl<br>Cardemil Herrera, Carmen (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Fondo de Cultura Económica S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'></td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>1996-01-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>2</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-8821-01-2</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Mi pequeño Chef, de cumpleaños</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Silva Bafalluy, María Luisa<br>Schkolnik Chamudes, Nora Lia (Ilustrador)</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>NESTLÉ Chile S.A.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2009-08-31</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-8868-01-7</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Rojo corazón</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Ediciones Ekaré Sur Ltda.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2009-12-01</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-8868-24-6</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Láminas rojo corazón</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Ediciones Ekaré Sur Ltda.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2015-11-02</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr><tr><td align='right' class = 'viñetaGreen' valign='top'>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class='textBoxGray'>ISBN:</td><td class='textBoxGrayDraw'>978-956-8868-41-3</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Título:</td><td class='textBoxGrayDraw'>Rojo corazón </td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Autor:</td><td class='textBoxGrayDraw'>Schkolnik Bendersky, Saúl</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Editorial:</td><td class='textBoxGrayDraw'>Ediciones Ekaré Sur Ltda.</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Materia:</td><td class='textBoxGrayDraw'>Literatura infantil</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Publicado:</td><td class='textBoxGrayDraw'>2016-03-24</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>NºEdición:</td><td class='textBoxGrayDraw'>1</td></tr>
<tr><td>&nbsp;</td><td class='textBoxGray'>Idioma:</td><td class='textBoxGrayDraw'>Español</td></tr>
<tr><td colspan="2">-------</td></tr>  <tr>
    <td colspan="3">
      <table width="100%" class="titletable">
        <tr>
					<td><a href="buscador.php">Nueva b&uacute;squeda</a></td>
          <td>128 resultados encontrados.</td>
					<td align="center">P&aacute;gina 9 / 9</td>
					<td align="right"><table><tr><td><a href="/site_isbn/buscador.php?mode=buscar&amp;code=&amp;tit_nombre=&amp;col_nombre=schkolnik&amp;tit_IDmateria=&amp;t_idiomas=&amp;tit_date_apar=&amp;D_sigP==&amp;pagina=8">&lt;&lt;</a></td><td>&gt;&gt;</td></tr></table></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
</div>



"""
text=text.replace("'","")
text=text.replace('"','')
text=text.replace(" class = viñetaGreen valign=top>&nbsp;&nbsp;&nbsp;&nbsp;&rsaquo;&rsaquo;&nbsp;&nbsp;</td><td class=textBoxGray","")
text=text.replace("<tr><td>&nbsp;</td><td class=textBoxGray>","")
text=text.replace("</td><td class=textBoxGrayDraw>"," ")
text=text.replace("</td></tr>","")
text=text.replace("<tr><td","")
text=text.replace("<br>","; ")

libro=[]
text=text.split("""colspan=2""")
for n in range (0,len(text)):
    if "Autor" in text[n]:
        if "titletable" in text[n]:
            libro.append(text[n].split("align=right>")[2])
        else:
            libro.append(text[n].split("align=right>")[1])

print(len(libro))
for x,l in enumerate(libro):
    print(x+1)
    print (l)
