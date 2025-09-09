from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List

from flask import Flask, render_template, url_for


def create_app() -> Flask:
	app = Flask(
		__name__,
		static_folder="static",
		template_folder="templates",
	)

	@app.context_processor
	def inject_globals() -> Dict[str, Any]:
		return {
			"url_for": url_for,
		}

	@app.route("/")
	def dashboard() -> str:
		context: Dict[str, Any] = {
			"username": "Usuário",
			"perfil": "admin",
			"data_atual": datetime.now().strftime("%d/%m/%Y"),
			"total_funcionarios": 120,
			"cadastrados_hoje": 3,
			"total_ativos": 100,
			"funcionarios_com_face": 80,
			"funcionarios_com_ponto_hoje": 95,
			"pontos_hoje": 340,
			"ultimos_pontos": [
				{"nome": "Ana Souza", "matricula": "12345", "data_hora": datetime.now()},
				{"nome": "João Lima", "matricula": "12346", "data_hora": datetime.now()},
			],
			"setores": [
				{"setor": "Enfermagem", "total": 40, "ativos": 34},
				{"setor": "Administração", "total": 20, "ativos": 18},
				{"setor": "UTI", "total": 25, "ativos": 22},
			],
			"funcionarios_recentes": [
				{"nome": "Carlos Silva", "setor": "Enfermagem", "data_cadastro": datetime.now()},
				{"nome": "Mariana Alves", "setor": "UTI", "data_cadastro": datetime.now()},
			],
		}
		return render_template("dashboard.html", **context)

	return app

