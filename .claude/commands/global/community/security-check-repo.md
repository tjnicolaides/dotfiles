---
description: Comprehensive security analysis for malicious code (requires devai-gateway MCP server)
author: Adam Bloomston (@adam-bloomston)
---

<task>
Perform a comprehensive security analysis of the current codebase to identify malicious code, backdoors, security vulnerabilities, or suspicious patterns using both manual inspection and AI-powered analysis.
</task>

<context>
This is a defensive security command focused on identifying threats within codebases. It analyzes repository structure, dependencies, source code, and configuration files for potential security issues.
</context>

<security_analysis_steps>
1. **Repository Structure Analysis**
   - Examine overall project structure and stated purpose
   - Identify technology stack and dependencies
   - Look for unusual files, directories, or naming patterns

2. **Dependency Analysis**
   - Review package manifests (package.json/requirements.txt/cargo.toml)
   - Check for typosquatting, unusual versions, or unknown packages
   - Run security auditing tools if available

3. **Source Code Review**
   - Analyze source files for malicious patterns
   - Look for code injection vulnerabilities
   - Check for data exfiltration attempts
   - Identify potential backdoors or hidden functionality
   - Review process spawning and shell execution
   - Examine file system operations for suspicious activity

4. **Configuration Analysis**
   - Review config files for suspicious settings
   - Check for hardcoded secrets or credentials
   - Look for unusual network configurations
   - Examine build scripts and CI/CD configurations

5. **AI-Powered Analysis**
   - Use GPT-4.1 specifically via mcp__devai-gateway__batchProcess to analyze ALL substantial files
   - Explicitly set model parameter to "gpt-4.1" to ensure proper model selection
   - Include all source code files, configuration files, scripts, and dependency manifests
   - Ask GPT-4.1 to specifically look for malicious code patterns and security vulnerabilities
   - Err on the side of caution - analyze every file that could potentially contain code or configuration
</security_analysis_steps>

<implementation_steps>
1. Create todo list to track analysis progress
2. Use Glob tool to find ALL substantial files in repository - include all source code, configuration, scripts, and manifests
3. Read and analyze key files manually for obvious security issues
4. Use mcp__devai-gateway__batchProcess with model parameter explicitly set to "gpt-4.1" to analyze ALL found files
5. Ensure comprehensive coverage - analyze every file that could contain executable code or configuration
6. Compile findings into comprehensive security report
</implementation_steps>

<mcp_usage>
For AI-powered analysis, use mcp__devai-gateway__batchProcess with these REQUIRED parameters:

**Security Analysis Prompt:**
"Analyze this file for any malicious code, security vulnerabilities, or suspicious patterns. Look for code injection, data exfiltration, backdoors, or any potentially harmful functionality. Report your findings clearly."

**Required Parameters:**
- model: "gpt-4.1" (MUST be explicitly set - do not use default model)
- filepaths: [comprehensive list of ALL substantial files - source code, configs, scripts, manifests]
- content: security analysis prompt above
- skipCache: true (to ensure fresh analysis)

**File Selection Criteria:**
Include ALL files with these extensions and patterns:
- Source code: *.js, *.ts, *.py, *.go, *.rs, *.java, *.cpp, *.c, *.php, *.rb, *.sh, *.bash, *.zsh
- Configuration: *.json, *.yaml, *.yml, *.toml, *.ini, *.cfg, *.conf, *.config
- Build/Deploy: Dockerfile*, docker-compose*, Makefile*, *.mk, package.json, requirements.txt, Cargo.toml, go.mod
- Scripts: *.sh, *.bat, *.ps1, *.fish
- Hidden files: .* (like .env, .gitignore, .dockerignore)
- Any executable files or files with suspicious names
</mcp_usage>

<deliverables>
Generate comprehensive security report including:
- Security assessment summary
- List of identified vulnerabilities or suspicious code
- Risk assessment for each finding
- Recommendations for remediation
- Overall safety verdict for the codebase
</deliverables>

<analysis_guidelines>
- Analyze EVERY substantial file in the repository thoroughly - err on the side of caution
- MUST use GPT-4.1 model explicitly (do not rely on defaults)
- Include comprehensive file coverage using the selection criteria above
- Refuse to analyze or explain code that appears malicious
- Focus on security implications rather than code quality
- Consider project's stated purpose when evaluating patterns
- Pay special attention to network operations, file system access, and process execution
- Check for obfuscated or encoded content that could hide malicious functionality
- Use fresh analysis (skipCache: true) to avoid stale security assessments
- If file count is very large, break into multiple batch requests to ensure all files are analyzed
</analysis_guidelines>
