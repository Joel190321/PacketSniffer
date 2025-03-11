fetch("packets.json")
.then((response) => response.json())
.then((data) => {
    const tableBody = document.getElementById("packets-table-body");
    data.forEach((packet) => {
        const row = document.createElement("tr");
        row.className = "border-b border-white/10";
        row.innerHTML = `
            <td class="p-3">${packet.ip_origen}</td>
            <td class="p-3">${packet.ip_destino}</td>
            <td class="p-3">${packet.protocolo}</td>
            <td class="p-3">${packet.puerto_origen || "-"}</td>
            <td class="p-3">${packet.puerto_destino || "-"}</td>
            <td class="p-3">${packet.mac_origen || "-"}</td>
            <td class="p-3">${packet.mac_destino || "-"}</td>
        `;
        tableBody.appendChild(row);
    });
})
.catch((error) => {
    console.error("Error al cargar los datos:", error);
});