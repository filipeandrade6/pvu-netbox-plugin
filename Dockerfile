ARG FROM_IMAGE=netboxcommunity/netbox
ARG FROM_TAG=latest-ldap
ARG FROM=${FROM_IMAGE}:${FROM_TAG}
FROM ${FROM}

ENV VIRTUAL_ENV=/opt/netbox/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY ./pvu_netbox_plugin /source/pvu-netbox-plugin/pvu_netbox_plugin/
COPY ./setup.py /source/pvu-netbox-plugin/
COPY ./pvu_netbox_plugin/templates ./
# COPY ./MANIFEST.in /source/pvu-plugin/
# COPY ./README.md /source/pvu-plugin/
# COPY --chown=1000:1000 --chmod=644 ./nextbox_ui_plugin/static/nextbox_ui_plugin /opt/netbox/netbox/static/nextbox_ui_plugin
# RUN pip3 install --no-cache-dir /source/pvu-plugin/
RUN /opt/netbox/venv/bin/pip install --no-cache-dir /source/pvu-netbox-plugin/