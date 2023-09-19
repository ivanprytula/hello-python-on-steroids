# Python interview questions

## Docker networks

When it comes to choosing the best Docker network for your Docker Compose setup, it depends on your specific requirements and the desired network topology. Here are a few options you can consider:

1. **Default network**: By default, Compose sets up a single network for your app. Each container for a service joins the default network and is both reachable by other containers on that network and discoverable by them at a hostname identical to the container name. This is the simplest option and works well for most use cases.

2. **Custom networks**: You can specify your own networks with the top-level `networks` key in your `docker-compose.yml` file. This allows you to create more complex topologies and specify custom network drivers and options. For example:

```yaml
networks:
  my_network:
    driver: bridge
```

Then, you can assign services to this custom network using the `networks` attribute:

```yaml
services:
  web:
    networks:
      - my_network
  db:
    networks:
      - my_network

```

This approach gives you more control over the network configuration.

3. **Host network**: If you want to use the host's networking stack directly, you can set the `network_mode` to `"host"` in your `docker-compose.yml` file. For example:

```yaml
services:
  web:
    network_mode: "host"
```

This allows containers to share the host's network namespace, making them accessible on the same IP address as the host.

## COPY vs ADD in Dockerfile

The **COPY** and **ADD** commands in a Dockerfile are similar but have some differences. Here's a summary of their key differences:

- **COPY**: The `COPY` instruction copies files from the build context or a URL to the container's filesystem at the specified destination path. It is a straightforward source-to-destination copy command and does not have additional features like tar extraction or remote URL support².

- **ADD**: The `ADD` instruction also copies files from the build context or a URL to the container's filesystem at the specified destination path. In addition to copying files, `ADD` has some extra functionality. It can handle local tar archives (in recognized compression formats) by unpacking them as directories. However, it does not decompress resources from remote URLs.

In general, it is recommended to use `COPY` instead of `ADD` unless you specifically need the additional features provided by `ADD`.

For more details and best practices, you can refer to the Docker documentation on [COPY](https://docs.docker.com/engine/reference/builder/#copy) and [ADD](https://docs.docker.com/engine/reference/builder/#add)

## Docker image optimization

<https://thegreencodes.com/docker-image-optimization-tips-and-tricks-for-faster-builds-and-smaller-sizes#heading-minimizing-the-number-of-layers>