{{- define "challenge-uncommon-imp.fullname" -}}
{{- default .Chart.Name .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "challenge-uncommon-imp.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "challenge-uncommon-imp.labels" -}}
{{- with .Values.labels }}
{{- toYaml . | nindent 4 }}
{{- end }}
{{- end }}
{{- define "challenge-uncommon-imp.selectorLabels" -}}
{{- if .Values.selectorLabels }}
{{- toYaml .Values.selectorLabels | nindent 4 }}
{{- else }}
{{- include "challenge-uncommon-imp.labels" . | nindent 4 }}
{{- end }}
{{- end }}

