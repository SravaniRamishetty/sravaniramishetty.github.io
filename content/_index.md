---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

sections:
  - block: about.avatar
    id: about
    content:
      title: ''
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
    design:
      columns: '1'
      background:
        color: 'white'
  - block: collection
    id: posts
    content:
      title: Recent Posts
      subtitle: ''
      text: ''
      # Choose how many pages you would like to display (0 = all pages)
      count: 5
      # Filter on criteria
      filters:
        folders:
          - post
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      view: compact
      columns: '1'
  - block: experience
    content:
      title: Experience
      # Date format for experience
      #   Refer to https://docs.hugoblox.com/customization/#date-format
      date_format: Jan 2006
      # Experiences.
      #   Add/remove as many `experience` items below as you like.
      #   Required fields are `title`, `company`, and `date_start`.
      #   Leave `date_end` empty if it's your current employer.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - title: Graduate Research Assitant
          company: Purdue University
          company_url: 'https://engineering.purdue.edu/ECE'
          company_logo: Purdue_Boilermakers_logo
          location: West Lafayette
          date_start: '2023-08-01'
          date_end: ''
          description: |2-
            Advisor: Prof. Eugenio Cullurciello
            
            Working on large language models and multi modal deep neural networks
        - title: Software Engineer Intern
          company: Amazon
          company_url: ''
          company_logo: 
          location: Austin
          date_start: '2022-09-01'
          date_end: '2022-12-03'
          description: Alexa devices
        - title: Graduate Teaching Assistant
          company: Purdue University
          company_url: 'https://engineering.purdue.edu/ECE'
          company_logo: Purdue_Boilermakers_logo
          location: West Lafayette
          date_start: '2023-08-15'
          date_end: '2023-12-31'
          description: For course ECE 60800 - computational models and methods. Instructed and evaluated students on course curriculum and semester projects
        - title: Graduate Teaching Assistant
          company: Purdue University
          company_url: 'https://engineering.purdue.edu/ECE'
          company_logo: Purdue_Boilermakers_logo
          location: West Lafayette
          date_start: '2022-01-15'
          date_end: '2023-05-31'
          description: For course ECE 20002. Instructed and evaluated students on course curriculum and semester projects
        - title: Data Engineer
          company: Citi Bank
          company_url: 'https://www.online.citibank.co.in/'
          company_logo: 
          location: Chennai, India
          date_start: '2018-07-04'
          date_end: '2021-07-31'
          description: |2-
              * Customer DNA and segmentation
              * Kafka event generation
              * Structuring digital forms unstructured data 
        - title: Research Assistant
          company: Indian Institute of Technology Madras (IITM)
          company_url: 'https://www.ee.iitm.ac.in/'
          company_logo: IIT-Madras-01
          location: Chennai
          date_start: '2017-05-01'
          date_end: '2018-07-31'
          description: |2-
            Advisor: Prof. Usha Mohan
            
            Optimizing efficiency of existing healthcare scheduling systems.
        - title: Research Intern
          company: Defense Research and Development Organization
          company_url: 'https://drdo.gov.in/drdo/'
          company_logo: 
          location: Chennai, India
          date_start: '2016-05-01'
          date_end: '2016-07-31'
          description: Improve reliability of LEON3 processors under high temperature and radiation conditions
    design:
      columns: '2'
---
