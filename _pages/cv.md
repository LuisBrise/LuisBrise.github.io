---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
- **Ph.D in Physical Sciences**  
  *Graduate Program in Physical Sciences* [PCF-UNAM](https://www.posgrado.fisica.unam.mx/) — **2027 (expected)**
  
- **M.S. in Physical Sciences**  
  *Graduate Program in Physical Sciences* [PCF-UNAM](https://www.posgrado.fisica.unam.mx/) — **2023**
  
- **B.S. in Physics**  
  [Facultad de Ciencias, UNAM](https://www.fciencias.unam.mx/) — **2019**

Research Appointments & Professional Experience
======
- **Ph.D. Guest Researcher** — *Uppsala University, Sweden*  
  **2025–2026**  
  Research on magnetic multislice methods, electron–matter interactions, and magnon EELS.

- **Ph.D. Researcher** — *UNAM*  
  **2023–Present**  
  Theoretical and computational studies of linear and angular momentum transfer from swift electrons to nanoparticles.

[comment]: <> (- **Modeling Analyst** — *Circana / Nielsen*)  
[comment]: <> (**2023–Present**)  
[comment]: <> (Development and optimization of large-scale marketing mix and econometric models.)
  
- **Master's Research Fellow** — *UNAM*  
  **2021–2023**  
  Theoretical and computational studies of linear and angular momentum transfer from swift electrons to nanoparticles.
  
Research Interests
======
- Electron–matter interactions  
- Theoretical electron microscopy  
- Angular and linear momentum transfer  
- Nanoplasmonics  
- Vibrational and magnetic EELS  
- High-performance scientific computing 

Publications (Selected)
======
  <ul>{% assign selected_pubs = site.publications | where: "selected", true %}
      {% for post in selected_pubs reversed %}
        {% include archive-single-cv.html %}
      {% endfor %}</ul>

Teaching Experience
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks & Conference Contributions (Selected)
======
  <ul>{% assign selected_talks = site.talks | where: "selected", true %}
      {% for post in selected_talks reversed %}
        {% include archive-single-cv.html %}
      {% endfor %}</ul>  
  
Service and leadership
======
- Organizer, *1st Meeting of Graduate Students of the Physics Department*, UNAM (2025)
- Treasurer, OPTICA Student Chapter, UNAM

Technical Skills 
======
- **Programming:** Python, C++, Fortran, R, SQL, Bash  
- **Scientific Computing:** FFT methods, numerical integration, multislice simulations  
- **Tools:** Git, VS Code, LaTeX, Mathematica, MATLAB  
- **HPC:** Parallelization, performance optimization, cluster workflows

Languages
======
- Spanish (native)  
- English (C1)

