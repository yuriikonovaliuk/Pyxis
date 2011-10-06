.DEFAULT_GOAL := collector-all
SHELL = /bin/bash

################ Constants ################

ADMINGUI_DIR := admingui
COLLECTOR_DIR := collector
GRAPHGUI_DIR := graphgui
LOGGER_DIR := logger

COMPONENT_CONF_FILE := comp.conf
PIP_REQUIRE := requirements.txt

COMPONENTS := all collector-all admingui-all graphgui-all collector admingui graphgui logger
SERVICES :=
SERVERS := beanstalkd
TARGETS := $(COMPONENTS) $(SERVICES) $(SERVERS)

################ Functions ################

echo_target_done = @echo Making $(1) done.

echo_target_started = @echo Making $(1).

define add_component
  @echo 'components+=( "$(1)" )' >> $(COMPONENT_CONF_FILE)
endef

define add_service
  @echo 'services+=( "$(1)" )' >> $(COMPONENT_CONF_FILE)
endef

define add_server
  @echo 'servers+=( "$(1)" )' >> $(COMPONENT_CONF_FILE)
endef

################  Targets  ################

.PHONY: $(TARGETS)

all: collector admingui graphgui logger
	$(call echo_target_done,$@)

collector-all: collector logger
	$(call echo_target_done,$@)

admingui-all: admingui logger
	$(call echo_target_done,$@)

graphgui-all: graphgui logger
	$(call echo_target_done,$@)

collector:
	$(call echo_target_started,$@)
	pip install -r $(COLLECTOR_DIR)/$(PIP_REQUIRE)
	
	$(call add_component,$@)

	$(call echo_target_done,$@)

admingui:
	$(call echo_target_started,$@)
	pip install -r $(ADMINGUI_DIR)/$(PIP_REQUIRE)
	
	$(call add_component,$@)
	
	$(call echo_target_done,$@)

graphgui:
	$(call echo_target_started,$@)
	pip install -r $(GRAPHGUI_DIR)/$(PIP_REQUIRE)
	
	$(call add_component,$@)
	
	$(call echo_target_done,$@)

logger:
	$(call echo_target_started,$@)
	pip install -r $(LOGGER_DIR)/$(PIP_REQUIRE)
	
	$(call add_component,$@)
	
	$(call echo_target_done,$@)

beanstalkd:
	$(call echo_target_started,$@)
	
	$(call add_server,$@)
	
	$(call echo_target_done,$@)

$(TARGETS): create_run_env

create_run_env:
	@echo Creating running environment.
	cp comp.conf.in comp.conf

