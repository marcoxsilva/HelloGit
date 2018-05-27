# Comandos

<ul>
	<li><h2>Sua Identidade</h2>
		<p>Temos que definir um nome de usuário e uma conta de email logo depois de instalar o git, pois todos os commits a patir de agora necessitaram dessas informaçoes.</p>
		<ul>
			<li><strong>$ git config --global user.name "Nome de usuário"</strong></li>
			<li><strong>$ git config --global user.email "Endereço de email do usuário"</strong></li>
		</ul>
	</li>
	<li><h2>Seu Editor</h2>
		<p>Definir um editor de texto padrão, por exemplo, caso voce queira utilizar o Emacs, use o seguinte comando:</p>
		<ul>
			<li><strong>$ git config --global core.editor emacs</strong></li>
		</ul>
	</li>
	<li><h2>Sua Ferramenta de Diff</h2>
		<p>Outra opção útil que você pode querer configurar é a ferramente padrão de diff utilizada para resolver conflitos de merge (fusão). Digamos que você queira utilizar o vimdiff:</p>
		<ul>
			<li><strong>$ git config --global merge.tool vimdiff</strong></li>
		</ul>
	</li>
	<li><h2>Verificando Suas Configurações</h2>
		<p>Caso queira verificar suas configurações, você pode utilizar o comando:</p>
		<ul>
			<li><strong>$ git config -l</strong> ou <strong>git config --list</strong></li>
		</ul>
	</li>
</ul>